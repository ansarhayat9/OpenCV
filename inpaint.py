import cv2

img=cv2.imread("image6.png")
mask=cv2.imread("mask.png",0)

pimg=cv2.inpaint(img,mask,2,cv2.INPAINT_NS)
pimg1=cv2.inpaint(img,mask,2,cv2.INPAINT_TELEA)

cv2.imshow("Original Image",img)
cv2.imshow("Inpaint Image1",pimg)
cv2.imshow("Inpaint Image2",pimg1)
cv2.waitKey(0)
cv2.destroyAllWindows()