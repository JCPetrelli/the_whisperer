import argparse
import os

def rename_video_in_folder(folder_path):
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: The specified folder '{folder_path}' does not exist.")
        return

    # List all files in the directory
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Filter out the video files (assuming .mp4 videos for simplicity)
    video_files = [f for f in files if f.endswith('.mp4')]
    
    # Check if there's exactly one video file
    if len(video_files) != 1:
        print(f"Error: There should be exactly one video file in the folder, but found {len(video_files)}.")
        return

    # Get the video file name
    video_file = video_files[0]

    # Extract the last folder name from the folder path
    last_folder_name = os.path.basename(os.path.normpath(folder_path))

    # Construct the new filename
    new_filename = f"{last_folder_name}_original.mp4"

    # Full paths for the current and new file locations
    current_path = os.path.join(folder_path, video_file)
    new_path = os.path.join(folder_path, new_filename)
    
    # Rename the file
    os.rename(current_path, new_path)
    print(f"Video file has been renamed to '{new_path}'.")

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Rename the sole video file in a specified directory.")

    # Add the argument
    parser.add_argument("folder_path", help="The local path to the folder containing exactly one video file to be renamed.")

    # Parse the argument
    args = parser.parse_args()

    # Execute the renaming operation
    rename_video_in_folder(args.folder_path)
