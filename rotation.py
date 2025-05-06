import cv2
# import numpy as np

img=cv2.imread("image1.jpg")
#To find image centre, half of width and height will be the cordinates of centre of image
width=img.shape[0]
height=img.shape[1]
centre=(height/2,width/2)

# For Transition
# x=100
# y=100
# M=np.float([[1,0,x],[0,1,y]])

# You can rotote imge from anywhere like (100,50) instead of centre
M=cv2.getRotationMatrix2D(centre,30,1)
img1=cv2.warpAffine(img,M,(height,width))

cv2.imshow("Original image",img)
cv2.imshow("Rotated image", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()