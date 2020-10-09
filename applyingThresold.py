import cv2
import imutils


img = cv2.imread("pythonlogo.jpg")

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresholdImg = cv2.threshold(grayImg,220,255,cv2.THRESH_BINARY)[1] #it returns two values and we need only last one.
# dst cv2.threshold(ser,threshold, maxValueForThreshold,binaryTupe)[1]  (Syntax)
thresholdImg2 = cv2.threshold(grayImg,150,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImage.jpg",thresholdImg)
cv2.imwrite("thresholdImage2.jpg",thresholdImg2)
