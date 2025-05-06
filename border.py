import cv2

img=cv2.imread("image1.jpg")

border=cv2.copyMakeBorder(img,20,20,20,20,borderType=cv2.BORDER_CONSTANT)

cv2.imshow("Borderd image", border)


cv2.waitKey(0)
cv2.destroyAllWindows()