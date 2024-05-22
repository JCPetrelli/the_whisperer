import sys
from datetime import datetime

def seconds_to_hms(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{int(h)}h {int(m)}m {int(s)}s"

def calculate_elapsed_time(file_path):
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        start_time_str = lines[0].strip().split(": ")[1]
        start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S.%f')
        end_time = datetime.now()
        elapsed_time_seconds = (end_time - start_time).total_seconds()
        elapsed_time_formatted = seconds_to_hms(elapsed_time_seconds)
        
        file.seek(0, 2) # Move to the end of the file
        file.write(f"\nEnd Time: {end_time.strftime('%Y-%m-%d %H:%M:%S.%f')}")
        file.write(f"\nElapsed Time: {elapsed_time_formatted}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python end_time.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    calculate_elapsed_time(file_path)
