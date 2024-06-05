import os
import sys
import pytube

def check_if_playlist(url):
    # Check if the URL is for a playlist
    return "list" in url

def append_playlist_links_to_file(url, file_path="list_of_videos.txt"):
    # Create a Playlist object using the URL
    playlist = pytube.Playlist(url)
    
    # Open the file in append mode
    with open(file_path, "a") as file:
        # Loop through the video URLs in the playlist
        for video_url in playlist.video_urls:
            file.write(video_url + "\n")

def main():
    # Check if the correct number of arguments was provided
    if len(sys.argv) != 2:
        # Incorrect number of arguments were provided, so print an error message and exit
        print("Incorrect number of arguments provided.")
        print("Usage: python3 append_to_list_from_playlist.py PLAYLIST_URL")
        sys.exit(1)

    # Get the playlist URL from the command line arguments
    url = sys.argv[1]
    
    # Check if the URL is a playlist
    if check_if_playlist(url):
        # Append the playlist links to the file
        append_playlist_links_to_file(url)
        print("Playlist links have been appended to 'list_of_videos.txt'")
    else:
        print("The provided URL is not a playlist.")

if __name__ == "__main__":
    main()
