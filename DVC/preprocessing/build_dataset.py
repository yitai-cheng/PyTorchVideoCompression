# import cv2
import os
current_directory = os.getcwd()
parent_DVC_directory = os.path.dirname(current_directory)

print(parent_DVC_directory)
exit(0)
videos_folder = os.path.join(parent_DVC_directory, "data/48Sequences-test")  # Path to the folder containing the frames

print(videos_folder)

# group_size = 7
# output_folder = "/Users/morphling/PyTorchVideoCompression/DVC/data/48Sequences-preprocessed"
# saved_frame_group_count = 0
#
# items = os.listdir(videos_folder)
# video_paths = [
#     os.path.join(videos_folder, item) for item in items if os.path.isfile(os.path.join(videos_folder, item))
# ]
#
# for i, video_path in enumerate(video_paths):
#
#     # Open the video file
#     # video_path = 'Gliding.mp4'
#     print("Extract frames from video:", video_path)
#
#     cap = cv2.VideoCapture(video_path)
#
#     # Check if video opened successfully
#     if not cap.isOpened():
#         print("Error: Could not open video.")
#         exit()
#
#     # Get the video's original FPS
#     fps = cap.get(cv2.CAP_PROP_FPS)
#
#     # Calculate the interval between the frames you want to capture
#     target_fps = 5
#     frame_interval = int(round(fps / target_fps))
#
#     count = 0  # To count frames
#     saved_frame_count = 0  # To count saved frames
#     frames = list()
#
#     while cap.isOpened():
#         ret, frame = cap.read()
#         # If read was successful, and we're at the correct interval, save the frame
#         if ret and count % frame_interval == 0:
#             frames += [frame]
#             #
#             # frame_filename = f"out-{saved_frame_count:02d}.jpeg"
#             # cv2.imwrite(frame_filename, frame)
#             # print(f"Saved {frame_filename}")
#             # saved_frame_count += 1
#         if not ret:
#             break  # Exit the loop if there are no frames left to read
#
#         count += 1
#
#     # Save the frames with the group size of 7
#     frames_count = len(frames)
#     print(f"Total frames: {frames_count}")
#     for i in range(0, frames_count - group_size + 1):
#         group = frames[i: i + group_size]
#         group_folder = os.path.join(output_folder, f"{saved_frame_group_count + i + 1:05d}")
#         os.makedirs(group_folder, exist_ok=True)
#         for j, frame in enumerate(group):
#             frame_filename = f"{group_folder}/im{j+1}.png"
#             cv2.imwrite(frame_filename, frame)
#             print(f"Saved {frame_filename}")
#
#     cap.release()
#     saved_frame_group_count += frames_count - group_size + 1
#     print("Done extracting frames.")
#     print("=====================================")

# List all entries in the given directory
entries = os.listdir(videos_folder)
training_list_path = os.path.join(parent_DVC_directory, "data/48Sequences-test/test.txt")
for entry in entries:
    for i in range(3, 8):
        with open(training_list_path, "a") as file:
            file.write(f"{entry}/im{i}.png\n")
