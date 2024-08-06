import cv2
import os

path = './pic/'
out_path = './mov/'
out_video_name = '2.11_28_1fps_reduced.mkv'
out_video_full_path = out_path + out_video_name

pre_imgs = os.listdir(path)
pre_imgs.sort()  # Ensure the images are in order
img = []

# Corrected the index increment and indexing of pre_imgs
x = 0
for i in range(17700, 17700 + 2 * len(pre_imgs), 2):
    pre_imgs[x] = str(i) + '.png'
    x += 1

# Create a list of image paths
for i in pre_imgs:
    i = path + i
    img.append(i)

# Get the size of the frames
frame = cv2.imread(img[0])
height, width, _ = frame.shape

# Scale down the resolution
scale_factor = 1  # Change this factor as needed to reduce the resolution
new_width = int(width * scale_factor)
new_height = int(height * scale_factor)
size = (new_width, new_height)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = 28  # Reduce frame rate to half of the original

video = cv2.VideoWriter(out_video_full_path, fourcc, fps, size)

for i in range(len(img)):
    frame = cv2.imread(img[i])
    resized_frame = cv2.resize(frame, size)
    video.write(resized_frame)

video.release()
print('Output video saved to', out_video_full_path)
