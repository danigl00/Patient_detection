import os

def access_files(directory):
    file_paths = []  # Create an empty list to store file paths
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if 'anonymized' not in file_path and '.mp4' in file_path:  # Example: Filter files based on conditions
                # Perform operations on the file_path
                file_paths.append(file_path)  # Append file_path to the list
                print(file_path)  # Example: Print the file path

    return file_paths  # Return the list of file paths

# Usage



if __name__ == "__main__":
    directory = 'I:/Chercheurs/Nguyen_DangKhoa/Projets_Recherche/Video/Video_original_mp4/'
    file_paths = access_files(directory)
    file_paths_set = set(file_paths)  # Convert the list to a set to remove duplicates
    duplicates = [file_path for file_path in file_paths if file_paths.count(file_path) > 1]  # Find duplicates in the list

    print('Number of files:', len(file_paths))  # Example: Print the number of files
    print('Number of duplicates:', len(duplicates))  # Example: Print the number of duplicates
    print('Duplicate file paths:', duplicates)  # Example: Print the duplicate file paths
