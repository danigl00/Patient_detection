import cv2

# Initialize variables to store the rectangle's starting and ending coordinates
start_point = None
end_point = None
drawing = False
rectangle_drawn = False

def normalize_coordinates(start_point, end_point, img):
    # Get the image size
    img_height, img_width = img.shape[:2]
    norm_start_point = (start_point[0]/img_height, start_point[1]/img_width)
    norm_end_point = (end_point[0]/img_height, end_point[1]/img_width)
    return  norm_start_point, norm_end_point

def get_bounding_box(start_point, end_point):
    y = (start_point[0] + end_point[0])/2
    x = (start_point[1] + end_point[1])/2
    h = abs(start_point[0] - end_point[0])
    w = abs(start_point[1] - end_point[1])
    print (f'Bounding box coordinates: {x}, {y}, {w}, {h}')
    return x, y, w, h

def save_annotations(x, y, w, h, patient, frame):
    with open('annotations.txt', 'a') as file:
        file.write(f'0 {x} {y} {w} {h}')

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global start_point, end_point, drawing, img, img_copy, rectangle_drawn

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        img = img_copy.copy() 
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)
            img_temp = img.copy()
            cv2.rectangle(img_temp, start_point, end_point, (0, 255, 0), 1)
            cv2.imshow('image', img_temp)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        cv2.rectangle(img, start_point, end_point, (0, 255, 0), 1)
        cv2.imshow('image', img)
        rectangle_drawn = True
        print(f'Rectangle coordinates: {start_point}, {end_point}')
    
# Load an image
img = cv2.imread('brain.jpg')
img_copy = img.copy()

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

while True:
    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == 13 and rectangle_drawn:  # Save on Enter key
        norm_start_point, norm_end_point = normalize_coordinates(start_point, end_point, img)
        x, y, w, h = get_bounding_box(norm_start_point, norm_end_point)
        save_annotations(x, y, w, h, 'patient1', 'frame1')
        rectangle_drawn = False
        
cv2.destroyAllWindows()

