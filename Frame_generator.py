import cv2
import random

def get_random_frame(video_path, output_path, frame):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # Set the frame position to a random frame number
    video.set(cv2.CAP_PROP_POS_FRAMES, random.randint(0, total_frames-1)) # random.randint(0, total_frames-1)
    # Read the frame
    ret, frame = video.read()
    
    # Check if the frame was read successfully
    if ret:
        # Save the frame as an image
        output_path = output_path.replace('.m2t', '.jpg')  # or '.png'
        cv2.imwrite(output_path, frame)
        print(f"Frame saved successfully in {output_path}.")
    else:
        print("Failed to obtain frame.")
    # Release the video file
    video.release()
    return frame

if __name__ == "__main__":
    frame = (2*60+54)*30
    for i in range(10):
        number = 1692 + i
        frame += 150
        filename = '5545721-3.m2t'
        get_random_frame(f'I:/Chercheurs/Nguyen_DangKhoa/Projets_Recherche/Video/Nouveau_nouveau_video_original/{filename}', 
                        f'C:/Users/p0121182/Project/Patient_detection/Dataset/{number}_{filename}',
                        frame)