import os
import subprocess

# Specify the input folder path
input_folder_path = "i:/Chercheurs/Nguyen_DangKhoa/Projets_Recherche/Video/Video_original/"

# Specify the output folder path
output_folder_path = "C:/Users/p0121182/Project/Patient_detection/Videosmp4/"

# Ensure the output folder exists
os.makedirs(output_folder_path, exist_ok=True)

# List all files in the input folder
files = os.listdir(input_folder_path)

# Iterate over each file
for file_name in files:
    # Check if the file has a .m2t extension
    if file_name.endswith(".m2t"):
        # Construct the full input file path
        input_file_path = os.path.join(input_folder_path, file_name)
        
        # Construct the output file path with .mp4 extension in the output folder
        output_file_name = file_name.replace(".m2t", ".mp4")
        output_file_path = os.path.join(output_folder_path, output_file_name)
        
        # Construct the ffmpeg command
        command = [
            "ffmpeg",
            "-i", input_file_path,
            "-vcodec", "copy",
            "-c:a", "aac",
            "-f", "mp4",
            output_file_path
        ]
        
        # Execute the ffmpeg command
        subprocess.run(command)
