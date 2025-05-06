import cv2

# Thresholding  can be applied only on Grayscale images
img=cv2.imread("image1.jpg",0)


# If pixel intensity value is
# greater than 100 = it set it to 255
# and if less than 100 = it set it to 0 (black)
_,th1=cv2.threshold(img,200,255,cv2.THRESH_BINARY)
cv2.imshow("original Image",img)
cv2.imshow("Simple Threshold Image",th1)


# th=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,197,7)
# cv2.imshow("Adaptive Threshold Image",th)

cv2.waitKey(0)
cv2.destroyAllWindows()