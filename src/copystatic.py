import os
import shutil


def copy_files_recursive(source_dir_path, dest_dir_path):
    #1: Wipe the destination directory
    if os.path.exists(dest_dir_path):
        print(f"Deleting existing directory: {dest_dir_path}")
        shutil.rmtree(dest_dir_path)

    #2: Create the fresh destination directory
    print(f"Creating directory: {dest_dir_path}")
    os.mkdir(dest_dir_path)

    #3: Loop everything inside the source directory
    for filename in os.listdir(source_dir_path):
        source_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        #4: Check if it's a file or another directory
        if os.path.isfile(source_path):
            print(f" * Copying file: {source_path} -> {dest_path}")
            shutil.copy(source_path, dest_path)
        else:
            copy_files_recursive(source_path, dest_path)