import cv2
import random

def get_random_frame(video_path, output_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # Set the frame position to a random frame number
    video.set(cv2.CAP_PROP_POS_FRAMES, random.randint(0, total_frames-1))
    # Read the frame
    ret, frame = video.read()
    
    # Check if the frame was read successfully
    if ret:
        # Save the frame as an image
        output_path = output_path.replace('.mp4', '.jpg')  # or '.png'
        cv2.imwrite(output_path, frame)
        print(f"Frame saved successfully in {output_path}.")
    else:
        print("Failed to obtain frame.")
    # Release the video file
    video.release()
    return frame

get_random_frame('I:/Chercheurs/Nguyen_DangKhoa/Projets_Recherche/Video/Video_original_mp4/Déjà_fait\p302-1.mp4', 
                 'C:/Users/p0121182/Project/Patient_detection/Dataset/1_1.mp4')  # Example: Get a random frame from a video and save it as an image