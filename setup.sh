#!/bin/bash

# Initialize variables
youtube_link=""
local_video_path=""
local_folder_path=""
project_name=""
stop_between_each_script=""

# Function to show usage
usage() {
    echo "Usage: $0 --p <Project Name> (--y <YouTube Link> | --l <Local Video Path>) | --lf <Local Folder Path>)"
    echo "Examples:"
    echo "  $0 --p my_project --y https://www.youtube.com/watch?v=dQw4w9WgXcQ --s false" 
    echo "  $0 --p my_project --l /path/to/local/video.mp4 --s false"
}

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --y) youtube_link="$2"; shift ;;
        --l) local_video_path="$2"; shift ;;
        --lf) local_folder_path="$2"; shift ;;
        --p) project_name="$2"; shift ;;
        --s) stop_between_each_script="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; usage; exit 1 ;;
    esac
    shift
done

# Check if the project name flag is provided
if [ -z "$project_name" ]; then
    echo "Error: You must specify a project name with --p."
    usage
    exit 1
fi

# Check if at least one of the video source flags is provided
if [ -z "$youtube_link" ] && [ -z "$local_video_path" ] && [ -z "$local_folder_path" ]; then
    echo "Error: You must specify either a YouTube link, a local video path, or a local folder path."
    usage
    exit 1
fi

# Check if the stop_between_each_script flag is provided
if [ -z "$stop_between_each_script" ]; then
    echo "Error: You must specify if you want to stop between each script with --s true."
    usage
    exit 1
fi

# Create project folder
if [ -n "$project_name" ]; then
    python3 create_project_folder.py --project "$project_name" 
fi

# Run the start time script
python3 start_time.py "$project_name/time_log.txt"

# Download video from youtube if necessary
if [ -n "$youtube_link" ]; then
    python3 interlude.py "Now i will download the video from youtube" "$stop_between_each_script"
    echo "Processing YouTube video link for project '$project_name': $youtube_link"
    python3 yt_download.py "$youtube_link" "$project_name"
    python3 rename_downloaded_video.py "$project_name/"
    python3 copy_videos_to_path.py "$project_name/${project_name}_original.mp4" "$project_name/"
fi

# Copy local video
if [ -n "$local_video_path" ]; then
    python3 interlude.py "Now i will copy the video and put it in the right place" "$stop_between_each_script"
    echo "Processing local video file for project '$project_name': $local_video_path"
    python3 copy_videos_to_path.py "$local_video_path" "$project_name/"
fi

# Copy local videos
if [ -n "$local_folder_path" ]; then
    python3 interlude.py "Now i will copy the videos and put them in the right place" "$stop_between_each_script"
    echo "Processing local video folder for project '$project_name': $local_folder_path"
    python3 copy_videos_to_path.py "$local_folder_path" "$project_name/"
fi

### TO RUN AT THE END OF EVERYTHING - Run the end time script
python3 end_time.py "$project_name/time_log.txt"