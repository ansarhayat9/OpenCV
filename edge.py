import cv2

img=cv2.imread("image1.jpg")
img1=cv2.imread("image5.png")
edge=cv2.Canny(img,100,100)

#adding Two images
#sum=cv2.addWeighted(img,0.8,img1,0.5,0)

cv2.imshow("Original Image1",img)
# cv2.imshow("Original Image2",img1)

#cv2.imshow("Sum Image",edge)

cv2.imshow("edged Image",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()