import cv2
import imutils


img = cv2.imread("pythonlogo.jpg")
gaussianBlur = cv2.GaussianBlur(img,(21,21),0)
#dst = cv2.GaussianBLur(src,(kernel),bordertype) (Syntax)
cv2.imwrite("gaussianImage.jpg",gaussianBlur)
