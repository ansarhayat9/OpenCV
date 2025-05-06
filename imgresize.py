import cv2

img = cv2.imread("image1.jpg")

# #riginal image
# cv2.imshow("Original Image",img)

#Dimension Perspective
# rsize = cv2.resize(img,(200,200),interpolation=cv2.INTER_AREA)

# Percentage Perspective
rsize = cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
cv2.imshow("Resize Image",rsize)

cv2.waitKey(0)