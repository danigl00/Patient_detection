import os
import cv2
import numpy as np
import random

def access_files(directory):
    file_paths = []  # Create an empty list to store file paths
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if 'classes' not in file_path and '.jpg' in file_path:
                file_paths.append(file_path)  # Append file_path to the list
    return file_paths

def differences_between_lists(list1, list2):
    base_names1 = [os.path.splitext(os.path.basename(file_path))[0] for file_path in list1]
    base_names2 = [os.path.splitext(os.path.basename(file_path))[0] for file_path in list2]
    differences = list(set(base_names1) - set(base_names2))
    return differences  # Return the differences

def mirror_images(image_path, output_directory):
    image = cv2.imread(image_path)  # Read the image
    mirrored_image = cv2.flip(image, 1)  # Flip the image
    name = f'{os.path.splitext(os.path.basename(image_path))[0]}_mirrored.jpg'  # Create a new name
    cv2.imwrite(f'{output_directory}{name}', mirrored_image)  # Save the mirrored image

def upside_down_images(image_path, output_directory):
    image = cv2.imread(image_path)  # Read the image
    upside_down_image = cv2.flip(image, 0)  # Flip the image
    name = f'{os.path.splitext(os.path.basename(image_path))[0]}_upside_down.jpg'  # Create a new name
    cv2.imwrite(f'{output_directory}{name}', upside_down_image)  # Save the mirrored image

def delete_redundat_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if 'mirrored' in file_path or 'upside_down' in file_path:
                os.remove(file_path)  # Remove the file

def add_noise(image_path, output_directory, degree_of_noise):
    image = cv2.imread(image_path) 
    noise = np.zeros_like(image)
    noisy_image = cv2.randn(noise, (0, 0, 0), (degree_of_noise, degree_of_noise, degree_of_noise))
    noisy_image = cv2.add(image, noisy_image)
    name = f'{os.path.splitext(os.path.basename(image_path))[0]}_noisy.jpg'  
    cv2.imwrite(f'{output_directory}{name}', noisy_image)  # Save the noisy image

def blur_images(image_path, output_directory):
    image = cv2.imread(image_path)  # Read the image
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)  # Blur the image
    name = f'{os.path.splitext(os.path.basename(image_path))[0]}_blurred.jpg'  # Create a new name
    cv2.imwrite(f'{output_directory}{name}', blurred_image)  # Save the blurred image


file_paths = access_files('C:/Users/p0121182/Project/Patient_detection/Dataset/')
length = len(file_paths)
output_directory = 'C:/Users/p0121182/Project/Patient_detection/Dataset/Noise/'
"""for file_path in file_paths:
    print(f'Processing image {file_paths.index(file_path) + 1}/{length}')
    degree_of_noise = random.randint(25, 110)
    add_noise(file_path, output_directory, degree_of_noise)"""

delete_redundat_files('C:/Users/p0121182/Project/Patient_detection/Dataset/Augmented/Noise/')