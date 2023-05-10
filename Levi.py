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