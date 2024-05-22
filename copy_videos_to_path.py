import argparse
import shutil
import os

def copy_and_rename_videos(source, target_dir):
    # List of accepted video file extensions
    valid_extensions = ['.mp4', '.mov', '.m4v', '.jpg', '.jpeg', '.png']
    
    video_files = []
    if os.path.isfile(source):
        # If source is a file, check if it matches the valid extensions
        if any(source.lower().endswith(ext) for ext in valid_extensions):
            video_files.append(os.path.basename(source))
        source_dir = os.path.dirname(source)
    elif os.path.isdir(source):
        # If source is a directory, find all files with valid extensions
        files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
        video_files = [f for f in files if any(f.lower().endswith(ext) for ext in valid_extensions)]
        source_dir = source
    else:
        print(f"Error: The source '{source}' is neither a valid file nor a directory.")
        return

    # Ensure the target directory exists, if not, create it
    full_target_dir = os.path.join(target_dir, "original_videos")
    if not os.path.isdir(full_target_dir):
        print(f"Warning: The target directory '{full_target_dir}' does not exist. Creating it.")
        os.makedirs(full_target_dir)

    # Get the project name from the target_dir
    project_name = target_dir.replace('/', '')

    # Process each video file
    for index, filename in enumerate(video_files, 1):
        extension = os.path.splitext(filename)[1]
        source_path = os.path.join(source_dir, filename)
        new_filename = f"{project_name}_original{index}{extension}"
        target_path = os.path.join(full_target_dir, new_filename)

        # Copy and rename the file
        shutil.copy2(source_path, target_path)
        print(f"File '{source_path}' has been copied and renamed to '{target_path}'.")

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Copy and rename video files from a specified directory or file.")

    # Add the arguments
    parser.add_argument("source", help="The local path to the video file or directory containing video files to be copied and renamed.")
    parser.add_argument("target_dir", help="The local path to the target directory where the videos will be copied and renamed.")

    # Parse the arguments
    args = parser.parse_args()

    # Execute the copy and rename operation
    copy_and_rename_videos(args.source, args.target_dir)
