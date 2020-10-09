import cv2
import time
cam = cv2.VideoCapture(0)   # initialize camera and check with it 0, 1 or 2
time.sleep(1)

while True:
    _,img = cam.read() # Read from camera
    cv2.imshow("cameraFeed",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):     # Press q to terminate
        break

cam.release()
cv2.destroyAllWindows()
 
