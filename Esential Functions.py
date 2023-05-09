import os
import shutil


# Scans Directories for  files and returns list of file paths found in directory - Adrian

def scan_directory(directory):
    files = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            files.append(file_path)
    return files


# Sorts files by their appropirate file extentions- Adrian

def sort_files(files):
    sorted_files = {}
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension not in sorted_files:
            sorted_files[file_extension] = []
        sorted_files[file_extension].append(file)
    return sorted_files


# Creates subdirectories for different types of files- Adrian

def create_subdirectories(directory, extensions):
    for extension in extensions:
        subdirectory = os.path.join(directory, extension[1:])
        if not os.path.exists(subdirectory):
            os.makedirs(subdirectory)


# Move files to appropriate subdirectories based on their file extensions- Adrian

def move_files(sorted_files, directory):
    for extension, files in sorted_files.items():
        subdirectory = os.path.join(directory, extension[1:])
        for file in files:
            destination = os.path.join(subdirectory, os.path.basename(file))
            try:
                shutil.move(file, destination)
                print(f"Moved {file} to {destination}")
            except Exception as e:
                print(f"Failed to move {file}: {str(e)}")


# Enter the Path to the directory you want sorted- Adrian
directory_path = "/path/to/directory"

# Scan directory for files- Adrian
files = scan_directory(directory_path)

# Sort files by type- Adrian
sorted_files = sort_files(files)

# Create subdirectories for different types of files- Adrian
create_subdirectories(directory_path, sorted_files.keys())

# Move files to appropriate subdirectories- Adrian
move_files(sorted_files, directory_path)
