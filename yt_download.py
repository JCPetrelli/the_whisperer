import os
import sys
import pytube
from pytube.cli import on_progress
import tqdm
from unidecode import unidecode
import re

########## DESCRIPTION ##########
### The Steam-Powered Stream Snatcher
### "The Ultimate Tool for Harvesting YouTube Videos with Elegance and Efficiency"
# This little script will download youtube videos for you.
### Characteristics:
# - It's a CLI (Command Line Interface) script so must be used in this way: "python3 yt_download.py URL [DESTINATION]"
# - The URL can either be a single video or a playlist of videos to download
# - The DESTINATION parameter is optional: if not specified it will save the files in the folder "downloads".
# - You can see the progress thanks to a not-so-fancy-but-cool progress bar
# - The file downloaded will have a safe filename (no spaces or strange characters whatsover)
# - You can decide if you want the HIGHEST QUALITY possible (slow and big download) or a discrete quality (faster download)
#   by Setting the variable "i_want_the_highest_quality" to True or False.
# - Do not worry for destinations not existing: it will create them for you.
#################################

i_want_the_highest_quality = True

def check_if_video_or_playlist(url):
    # Check if the URL is for a playlist or a single video
    if "list" in url:
        # URL is for a playlist
        return "playlist"
    else:
        # URL is for a single video
        return "video"

def make_safe(filename):
    # Remove special characters and spaces
    safe_filename = re.sub(r'[^\w\s]', '', filename)
    # Replace remaining spaces with underscores
    safe_filename = safe_filename.replace(' ', '_')
    # Convert non-ASCII characters to their closest ASCII equivalents
    safe_filename = unidecode(safe_filename)
    return safe_filename

def download_video(url, destination):
    # Create a YouTube object using the URL
    yt = pytube.YouTube(url, on_progress_callback=on_progress)
    video_title = yt.title
    print(f"Downloading: '{video_title}' ...")
    video_title_safe_for_filename = make_safe(video_title)
    
    if i_want_the_highest_quality:

        # Check if the temporary folder exists and create it if it doesn't
        temp_folder = "temp_folder"

        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
            print(f"Folder '{temp_folder}' created!")

        print("Downloading the highest-possible quality video ...")
        video_file_name = "video.mp4"
        yt.streams.filter(adaptive=True).order_by('resolution').desc().first().download(output_path=temp_folder, filename=video_file_name)

        print("Downloading the audio ... ")
        audio_file_name = "audio.mp3"
        audio_stream = yt.streams.filter(adaptive=True, only_audio=True).first()
        # Download the audio to a file with the custom name
        audio_stream.download(output_path=temp_folder, filename=audio_file_name)

        import subprocess

        # Set the input audio and video files
        audio_file = f"{temp_folder}/audio.mp3"
        video_file = f"{temp_folder}/video.mp4"

        # Set the output video file
        output_file = f"{destination}/{video_title_safe_for_filename}.mp4"

        # Use ffmpeg to combine the audio and video
        subprocess.run(["ffmpeg", "-i", audio_file, "-i", video_file, "-c", "copy", output_file])
        print("Combined audio and video successfully")

        ### Clean-up by removing the 'temp_folder' completely
        # Check if the folder exists
        if not os.path.exists(temp_folder):
            print(f"{temp_folder} does not exist")
            return

        # Remove all contents of the folder (if existing)
        for root, dirs, files in os.walk(temp_folder):
            print(root, dirs, files)
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                os.rmdir(os.path.join(root, d))

        # Remove the folder itself
        os.rmdir(temp_folder)

        return

    # If I do not need the highest quality, I take the fast approach
    video_title_safe_for_filename = video_title_safe_for_filename + ".mp4"
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=destination, filename=video_title_safe_for_filename)


def main():
    # Check if the correct number of arguments was provided
    if len(sys.argv) == 3:
        # Two arguments were provided, so use them as the URL and destination
        url = sys.argv[1]
        destination = sys.argv[2]
    elif len(sys.argv) == 2:
        # One argument was provided, so use it as the URL and set the destination to a default folder
        url = sys.argv[1]
        destination = "downloads"
    else:
        # Incorrect number of arguments were provided, so print an error message and exit
        print("Incorrect number of arguments provided.")
        print("Usage: python3 script.py URL [DESTINATION]")
        sys.exit(1)

    # Check if the destination folder exists and create it if it doesn't
    if not os.path.exists(destination):
        os.makedirs(destination)
        print(f"Folder '{destination}' created!")
    
    # Tell me if the URL is a single video or a playlist
    what_is_my_url = check_if_video_or_playlist(url)
    print(what_is_my_url)

    if what_is_my_url == "video":
        download_video(url, destination)
    
    if what_is_my_url == "playlist":
        p = pytube.Playlist(url)
        no_of_videos = p.length
        are_you_sure = input(f"Are you sure you want to download {no_of_videos} videos (Y/N)?")
        are_you_sure = are_you_sure.upper()
        if are_you_sure == "N":
            exit()
        for url in p.video_urls:
            download_video(url, destination)
        print(f"{no_of_videos} Videos Downloaded in '{destination}'!")

if __name__ == "__main__":
    main()
