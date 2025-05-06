import cv2
import numpy as np
img=cv2.imread("line.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edge=cv2.Canny(gray,100,100)

detectline=cv2.HoughLinesP(edge,1,np.pi/180,100,minLineLength=7,maxLineGap=10)

if detectline is not None:
    for points in detectline:
        x1,y1,x2,y2=points[0]
        cv2.line(img,(x1,y1),(x2,y2),255,3)
        
cv2.imshow("detected lines",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
        