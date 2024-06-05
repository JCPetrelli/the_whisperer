#!/bin/bash

# Function to check if a URL contains https
is_https_url() {
    if [[ $1 == https* ]]; then
        return 0
    else
        return 1
    fi
}

# Function to create a temporary directory and clean up afterward
with_temp_dir() {
    TEMP_DIR=$(mktemp -d)
    trap 'rm -rf "$TEMP_DIR"' EXIT
    echo "$TEMP_DIR"
}

# Function to make a filename websafe
make_websafe() {
    local name="$1"
    local base="${name%.*}"
    local ext="${name##*.}"
    local safe_base=$(echo "$base" | tr -cd '[:alnum:]' | tr '[:upper:]' '[:lower:]')
    local len=${#safe_base}
    if [ $len -gt 20 ]; then
        safe_base="${safe_base:0:10}${safe_base: -10}"
    fi
    echo "${safe_base}.${ext}"
}

# Check if the argument is an HTTPS URL
if is_https_url "$1"; then
    URL="$1"
    DESTINATION=$(with_temp_dir)
    python3 yt_download.py "$URL" "$DESTINATION"

    # Get the name of the downloaded video file
    VIDEO_FILE=$(find "$DESTINATION" -type f -name '*.mp4' -o -name '*.mkv' -o -name '*.webm' | head -n 1)
    VIDEO_NAME=$(basename "$VIDEO_FILE")
    VIDEO_NAME_WITHOUT_EXT="${VIDEO_NAME%.*}"

    # Create a new folder with the name of the video (minus the extension)
    mkdir "$VIDEO_NAME_WITHOUT_EXT"
    mv "$VIDEO_FILE" "$VIDEO_NAME_WITHOUT_EXT/"
    echo "Video moved to folder: $VIDEO_NAME_WITHOUT_EXT"

    ### Run whisper on the video file
    ### Remember to uncomment / comment the lines that you want

    ### Default way to translate a video:
    #whisper "$VIDEO_NAME_WITHOUT_EXT/$VIDEO_NAME" --model medium --task translate --output_format all --output_dir "$VIDEO_NAME_WITHOUT_EXT/"

    ### Default way to transcribe a video:
    #whisper "$VIDEO_NAME_WITHOUT_EXT/$VIDEO_NAME" --model medium --task transcribe --output_format all --output_dir "$VIDEO_NAME_WITHOUT_EXT/"

    ### Other ways to run whisper on the file. 

    # Translate to english and set --max_line_width to 42 and --max_line_count to 2
    whisper "$VIDEO_NAME_WITHOUT_EXT/$VIDEO_NAME" --model medium --task translate --output_format all --output_dir "$VIDEO_NAME_WITHOUT_EXT/" --word_timestamps True --max_line_width 42 --max_line_count 2

    # Transcribe in the original language and set --max_line_width to 42 and --max_line_count to 2
    #whisper "$VIDEO_NAME_WITHOUT_EXT/$VIDEO_NAME" --model medium --task translate --output_format all --output_dir "$VIDEO_NAME_WITHOUT_EXT/" --word_timestamps True --max_line_width 42 --max_line_count 2

    echo "Whisper command executed on video: $VIDEO_NAME_WITHOUT_EXT/$VIDEO_NAME"
else
    # If it's a local file
    FILE_PATH="$1"
    FILE_NAME=$(basename "$FILE_PATH")
    SAFE_NAME=$(make_websafe "$FILE_NAME")
    FILE_EXT="${SAFE_NAME##*.}"
    SAFE_BASE="${SAFE_NAME%.*}"

    # Create a new folder with the websafe name (minus the extension)
    mkdir "$SAFE_BASE"
    cp "$FILE_PATH" "$SAFE_BASE/$SAFE_NAME"
    echo "Local file copied to: $SAFE_BASE/$SAFE_NAME"

    # Run whisper on the local file
    whisper "$SAFE_BASE/$SAFE_NAME" --model medium --task translate --output_format all --output_dir "$SAFE_BASE/"
    echo "Whisper command executed on local file: $SAFE_BASE/$SAFE_NAME"
fi
