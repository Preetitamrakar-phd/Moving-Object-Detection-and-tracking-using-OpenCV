import cv2
import imutils # used for resizing, resahping, croping

img = cv2.imread("pythonlogo.jpg")
resizeImg = imutils.resize(img,width=20)
cv2.imwrite("resizedImg.jpg",resizeImg)
