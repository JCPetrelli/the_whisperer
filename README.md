# The Whisperer
## How to use

### From youtube playlist to your local list of videos
You want to get all the video files links from youtube running the following command:
`python3 append_to_list_from_playlist.py "https://www.youtube.com/watch?v=VpLh--NMCI0&list=PLY39OOz2pq2vcZqIXMGGPZVlWCo_3D5S0&pp=iAQB"`

(To find the link to the playlist just go to the channel you want, click on playlists and save the link from a playlist)
Tip: Enclose the link between " ".

### Check the list of links "list_of_videos.txt"
To see if you really want all those links. Could be that you forgot to delete the previously processed links.
Please notice: You can also add paths to local files if you want to process those instead of youtube links. Just add them to the list.

### Run './process_list.sh'
And it will process all the videos one by one.

### If you want to process only one video
Just run:
`./process_video.sh "YOUTUBELINK OR LOCAL PATH"`


### Standards for Subtitles

The standard size and format for good subtitles in movies can vary slightly depending on the guidelines of different organizations or personal preferences. However, a commonly accepted standard includes the following elements:

- Character Length: Subtitles should generally not exceed 32-42 characters per line.
- Line Count: Subtitles should be limited to a maximum of 2 lines per subtitle block.
- Reading Speed: Subtitles should be displayed long enough for viewers to read comfortably, typically around 150-180 words per minute.
- Timing: Each subtitle should appear on screen for a minimum of 1-1.5 seconds per line and stay long enough to be read twice.
- Font Size and Style: A clear, sans-serif font such as Arial or Helvetica is preferred, usually in white with a thin black outline or shadow for readability against various backgrounds.
- Position: Subtitles are usually positioned at the bottom center of the screen, avoiding important visual elements whenever possible.


### How to add subtitles to YouTube

To add subtitles to a YouTube video, you typically need to use a file like .srt or .vtt. 

Here are the steps to upload subtitles to YouTube:

1 - Sign in to YouTube Studio: Go to YouTube Studio and sign in with your Google account.
2 - Go to Videos: In the left-hand menu, click on "Content" to see your uploaded videos.
3 - Select the Video: Click on the video to which you want to add subtitles.
4 - Open Subtitles Menu: In the video details page, click on "Subtitles" in the left-hand menu or at the top bar if you are editing a specific video.
5 - Add Language: If you haven't added any subtitles yet, click on "Add Language" and select the language of your subtitles.
6 - Upload Subtitles: Click on "Add" under subtitles for the selected language. Then, choose "Upload file".
7 - Choose File Type: Select the file type as "With timing" since your .srt and .vtt files contain timing information.
8 - Upload File: Click on "Continue" and then "Choose file" to upload your .srt or .vtt file from your computer.
9 - Review and Save: Review the subtitles to make sure they sync correctly with the video. Click on "Save" to publish the subtitles.