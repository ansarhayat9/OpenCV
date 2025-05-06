import cv2
img=cv2.imread("image5.png")

dimg=cv2.fastNlMeansDenoisingColored(img,None,15,15,10)
# bilateral filter 
bdimg=cv2.bilateralFilter(img,10,70,70)

cv2.imshow("Original Img",img)
cv2.imshow("Denoised Image",dimg)
cv2.imshow("Bilateral Denoised Image",bdimg)
cv2.waitKey(0)
cv2.destroyAllWindows()