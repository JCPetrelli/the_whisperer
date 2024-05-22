import argparse
import os

# Run like this: python3 create_project_folder.py --project my_project

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Create a project folder.')

    # Add the arguments
    parser.add_argument('--project', type=str, help='The name of the project folder to create', required=True)

    # Execute the parse_args() method
    args = parser.parse_args()

    project_name = args.project

    # Check if the folder already exists
    if not os.path.exists(project_name):
        os.makedirs(project_name)
        print(f'Folder "{project_name}" created successfully.')
    else:
        print(f'Folder "{project_name}" already exists.')

if __name__ == "__main__":
    main()
