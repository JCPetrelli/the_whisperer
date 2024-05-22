import sys
from datetime import datetime

def save_start_time(file_path):
    with open(file_path, 'w') as file:
        start_time = datetime.now()
        file.write(f"Start Time: {start_time.strftime('%Y-%m-%d %H:%M:%S.%f')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python start_time.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    save_start_time(file_path)
