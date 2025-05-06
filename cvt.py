import cv2

img=cv2.imread("image1.jpg")

img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2LUV)
img4=cv2.cvtColor(img,cv2.COLOR_BGR2XYZ)

cv2.imshow("Original Image",img)
cv2.imshow("Image with Different Color1",img1)
cv2.imshow("Image with Different Color2",img2)
cv2.imshow("Image with Different Color3",img3)
cv2.imshow("Image with Different Color4",img4)
cv2.waitKey(0)
cv2.destroyAllWindows()