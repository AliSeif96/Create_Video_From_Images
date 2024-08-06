# new version of create video from .png files 

```ruby
ffmpeg -i input.mp4 -c:v libx265 -crf 28 output.mp4
```




# Create_Video_From_Images
Create Video From Images

```ruby

import cv2
import os
name='Degree_Radian=1.543'
path = 'G:/New Two jump first order transition (Not Scale)/Cpp/Change a algorithm seif/Plot/'+name+'/'
out_path = 'G:/New Two jump first order transition (Not Scale)/Cpp/Change a algorithm seif/Plot/'
out_video_name = name+'.mp4'
out_video_full_path = out_path+out_video_name

pre_imgs = os.listdir(path)
img = []

for i in range(len(pre_imgs)): 
    if i%10==0:
        pre_imgs[i]=str(i/100)+'0.png'
    else:
        pre_imgs[i]=str(i/100)+'.png'
for i in pre_imgs:
    i = path+i
    #print(h)
    img.append(i)
    #i=i+1

#print(img)

cv2_fourcc = cv2.VideoWriter_fourcc(*'.avi')

frame = cv2.imread(img[0])
size = list(frame.shape)
del size[2]
size.reverse()
print(size)

video = cv2.VideoWriter(out_video_full_path, cv2_fourcc, 8, size) #output video name, fourcc, fps, size

for i in range(len(img)): 
    video.write(cv2.imread(img[i]))
    #print('frame ', i+1, ' of ', len(img))

video.release()
print('outputed video to ', out_path)


```
