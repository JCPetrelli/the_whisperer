#!/bin/bash

# Check if list_of_videos.txt exists
if [ ! -f list_of_videos.txt ]; then
    echo "list_of_videos.txt not found!"
    exit 1
fi

# Read the list_of_videos.txt file line by line
while IFS= read -r video_link; do
    # Skip empty lines
    if [ -z "$video_link" ]; then
        continue
    fi

    # Trim whitespace and process each video link
    video_link=$(echo "$video_link" | xargs)
    ./process_video.sh "$video_link"
    if [ $? -ne 0 ]; then
        echo "Error processing $video_link"
    fi
done < list_of_videos.txt
