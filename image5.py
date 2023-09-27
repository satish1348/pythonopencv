import cv2
im=cv2.imread('pxfuel.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Tom and jerry',im)
cv2.waitKey(0)
cv2.destroyAllWindow()