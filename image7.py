import cv2
image=cv2.imread("pxfuel.jpg")
alpha=0.9
beta=3
ad=cv2.convertScaleAbs(image,alpha=alpha,beta=beta)
cv2.imshow("adjusted",ad)
cv2.waitKey()
cv2.destroyAllWindows()