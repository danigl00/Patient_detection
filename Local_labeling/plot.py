import cv2
import numpy as np

# Read the values from the file
with open('Dataset/1657_5731012-2.txt', 'r') as file:
    line = file.readline().strip()

# Parse the line to extract the numbers
values = line.split()
_, center_x, center_y, width, height = map(float, values)

# Calculate the top-left and bottom-right coordinates
x1 = center_x - (width / 2)
y1 = center_y - (height / 2)
x2 = center_x + (width / 2)
y2 = center_y + (height / 2)

# Create a blank image (for demonstration purposes, let's create a 800x600 image)
image = cv2.imread('Dataset/1657_5731012-2.jpg')
# Convert normalized coordinates to pixel values
image_height, image_width = image.shape[:2]
x1_pixel = int(x1 * image_width)
y1_pixel = int(y1 * image_height)
x2_pixel = int(x2 * image_width)
y2_pixel = int(y2 * image_height)

centerx = int(center_x * image_width)
centery = int(center_y * image_height)
# Draw the rectangle on the image
cv2.rectangle(image, (x1_pixel, y1_pixel), (x2_pixel, y2_pixel), (0, 255, 0), 2)
cv2.circle(image, (centerx, centery), 5, (0, 0, 255), -1)


# Display the image
cv2.imshow('Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
