import cv2
img=cv2.imread("pxfuel.jpg")
img_v=cv2.flip(img,0)
cv2.imshow("vertical flip",img_v)
cv2.waitKey(0)
cv2.destroyAllWindows()