import cv2
import numpy as np

img=cv2.imread("image1.jpg")

# log transformation
def logtran(src):
    c=255/np.log(1+np.max(src))
    # c is a scaling constant given by 255/log(1+m)
    # where m is the maximum pixel value in image
    lt=c*np.log(1+src)
    lt=np.array(lt,dtype=np.uint8)
    return(lt)

# gamma transformation
def gammatran(src,gamma):
    gt=np.array(255*(img/255)**gamma,dtype=np.uint8)
    return(gt)

inttran=logtran(img)
inttran1=gammatran(img,3)

cv2.imshow("Original Image",img)
cv2.imshow("Log Transformed Image",inttran)
cv2.imshow("Gamma Transformed Image",inttran1)
cv2.waitKey(0)
cv2.destroyAllWindows()