import os

def access_files(directory):
    file_paths = []  # Create an empty list to store file paths
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if 'anonymized' not in file_path and '.m2t' in file_path:
                file_paths.append(file_path)  # Append file_path to the list
                print(file_path)  # Example: Print the file path

    return file_paths  # Return the list of file paths

def obtain_list_files(directory, file_filter):
    file_paths = []  # Create an empty list to store file paths
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_filter in file_path:
                file_paths.append(file_path)

    return file_paths  # Return the list of file paths

def differences_between_lists(list1, list2):
    base_names1 = [os.path.splitext(os.path.basename(file_path))[0] for file_path in list1]
    base_names2 = [os.path.splitext(os.path.basename(file_path))[0] for file_path in list2]
    differences = list(set(base_names1) - set(base_names2))
    return differences  # Return the differences


if __name__ == "__main__":
    directory = 'C:/Users/p0121182/Project/Patient_detection/Dataset/'
    file_paths_jpg = obtain_list_files(directory, file_filter='.jpg')
    file_paths_txt = obtain_list_files(directory, file_filter='.txt')

    print('Number of files:', len(file_paths_jpg))  # Example: Print the number of files
    print('Number of files:', len(file_paths_txt))  # Example: Print the number of files

    differences = differences_between_lists(file_paths_jpg, file_paths_txt)  # Example: Find differences between two lists
    print('Differences between lists:', differences)  # Example: Print the differences between two lists