
import cv2 
import os 
import time

# Define the duration (in seconds) of the video capture here
capture_duration = 210
  
# Read the video from specified path 
cam = cv2.VideoCapture("ele3.mp4") 
  
try: 
      
    # creating a folder named data 
    if not os.path.exists('videotoimage'): 
        os.makedirs('videotoimage') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# start frame for the slicing operation 
count = 0
  
start_time = time.time()
while( int(time.time() - start_time) < capture_duration ): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        name = './data/frame{:d}'+str(count) + '.jpg'
        print ('Creating...' + name) 
  
        # Delay to to get next frame
        count += 20 # i.e. at 30 fps, this advances one second
        cam.set(1, count)
        cv2.imwrite("videotoimage/"+str(count)+"p.jpg", frame) 
        cv2.waitKey(1)
        cv2.imshow(name,frame)
    else: 
        break

  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows()