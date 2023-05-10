import os
import shutil
import logging


# Scans Directories for files and returns list of file paths found in directory -Adrian
def scan_directory(directory):
    files = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            files.append(file_path)
    return files


# Sorts files by their appropriate file extensions -Adrian
def sort_files(files):
    sorted_files = {}
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension not in sorted_files:
            sorted_files[file_extension] = []
        sorted_files[file_extension].append(file)
    return sorted_files


# Creates subdirectories for different types of files -Adrian
def create_subdirectories(directory, extensions):
    for extension in extensions:
        subdirectory = os.path.join(directory, extension[1:])
        if not os.path.exists(subdirectory):
            os.makedirs(subdirectory)


# Move files to appropriate subdirectories based on their file extensions -Adrian
def move_files(sorted_files, directory, backup=False, log=False):
    for extension, files in sorted_files.items():
        subdirectory = os.path.join(directory, extension[1:])
        for file in files:
            destination = os.path.join(subdirectory, os.path.basename(file))
            if backup:
                try:
                    shutil.copy2(file, destination+".backup")
                    if log:
                        logging.info(f"Created backup copy of {file} as {destination}.backup")
                except Exception as e:
                    if log:
                        logging.error(f"Failed to create backup copy of {file}: {str(e)}")
            try:
                shutil.move(file, destination)
                if log:
                    logging.info(f"Moved {file} to {destination}")
            except Exception as e:
                if log:
                    logging.error(f"Failed to move {file}: {str(e)}")


# Renames a file -Jaylon
def rename_file(file, new_name, log=False):
    try:
        os.rename(file, new_name)
        if log:
            logging.info(f"Renamed {file} to {new_name}")
    except Exception as e:
        if log:
            logging.error(f"Failed to rename {file}: {str(e)}")


# Deletes empty directories -Jaylon
def delete_empty_directories(directory, log=False):
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                try:
                    os.rmdir(dir_path)
                    if log:
                        logging.info(f"Deleted empty directory {dir_path}")
                except OSError as e:
                    if log:
                        logging.error(f"Failed to delete empty directory {dir_path}: {e.strerror}")
                except Exception as e:
                    if log:
                        logging.error(f"An error occurred while deleting empty directory {dir_path}: {str(e)}")

# Prompt for the directory path to sort -Jaylon
directory_path = input("Enter the directory path to sort: ")

# Set up logging -Jaylon
log_dir = os.path.join(directory_path, "logs")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'file_sorter.log'), filemode='w', level=logging.INFO)

# Scan directory for files -Jaylon
files = scan_directory(directory_path)

# Sort files by type -Levi
sorted_files = sort_files(files)

# Create subdirectories for different types of files -Levi
create_subdirectories(directory_path, sorted_files.keys())

# Move files to appropriate subdirectories -Levi
move_files(sorted_files, directory_path, backup=True, log=True)

# Rename a file -Levi
file_to_rename = os.path.join(directory_path, "test.txt")

# Delete empty directories -Levi
delete_empty_directories(directory_path, log=True)