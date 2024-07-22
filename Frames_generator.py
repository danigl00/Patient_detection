import cv2
import random
import os
import Frame_generator
import Obtain_directory

output_folder = 'C:/Users/p0121182/Project/Patient_detection/Dataset/'
file_paths = Obtain_directory.access_files('I:/Chercheurs/Nguyen_DangKhoa/Projets_Recherche/Video/Video_original_mp4/')

corrected_file_paths = [path.replace('\\', '/') for path in file_paths]
print('Number of files:', len(file_paths))  # Example: Print the number of files
duplicates = [file_path for file_path in file_paths if file_paths.count(file_path) > 1]  # Find duplicates in the list
print('Number of duplicates:', len(duplicates))  # Example: Print the number of duplicates
print('Duplicate file paths:', duplicates)  # Example: Print the duplicate file paths
i = 757
for file_path in file_paths:
    file_name = os.path.basename(file_path)
    for _ in range(1):
        i += 1
        Frame_generator.get_random_frame(file_path, f'{output_folder}{i}_{file_name}')


