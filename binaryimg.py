import cv2
import numpy as np

M=np.zeros((500,500))

rectangle=cv2.rectangle(M.copy(),(50,50),(450,450),1,-1)
circle=cv2.circle(M.copy(),(250,250),250,1,-1)
sum=cv2.add(rectangle,circle)

# bitand=cv2.bitwise_and(rectangle,circle)
# bitor=cv2.bitwise_xor(rectangle,circle)

# cv2.imshow("rectangle",rectangle)
# cv2.imshow("circle",circle)

cv2.imshow("sum",sum)

# cv2.imshow("and",bitand)
# cv2.imshow("xor",bitor)
cv2.waitKey(0)
cv2.destroyAllWindows()
