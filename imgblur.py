import cv2

img = cv2.imread("image1.jpg")

#Gaussian Blur 
#Kernal values must be odd
gblur=cv2.GaussianBlur(img,(11,11),0)
cv2.imshow("Guassian Blur",gblur)

#Median Blur
mblur=cv2.medianBlur(img,11)
cv2.imshow("Median Blur",mblur)

#original
cv2.imshow("Original Image",img)

cv2.waitKey(0)

# good habit to ensure close
cv2.destroyAllWindows()