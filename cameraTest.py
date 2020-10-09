import cv2
import time
cam = cv2.VideoCapture(0)   # initialize camera and check with it 0, 1 or 2
time.sleep(1)

_,img = cam.read() # Read from camera
cv2.imwrite("cameraImg.jpg",img)

cam.release()
 
