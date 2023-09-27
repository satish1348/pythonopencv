import cv2 
import numpy as np

image = cv2.imread("pxfuel.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred =cv2.GaussianBlur(gray,(5,5),0)
wide = cv2.Canny(blurred, 50, 200)
mid = cv2.Canny(blurred, 30,150)
tight =cv2.Canny(blurred, 210,250)
def auto_canny_edge_detection(image, sigma=0.33):
	md= np.median(image)
	lower_value = int(max(0,(1.0-sigma) *md))
	upper_value = int(min(255,(1.0+sigma) *md))
	return cv2.Canny(image,lower_value, upper_value)
auto_edge = auto_canny_edge_detection(blurred)
cv2.imwrite("auto.jpg",auto_edge)