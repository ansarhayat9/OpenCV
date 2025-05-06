import cv2

img=cv2.imread("image4.png")

# line=cv2.arrowedLine(img,(0,0),(400,600),(255),10)
text=cv2.putText(img,"python",(150,50),cv2.FONT_HERSHEY_DUPLEX,2,255,2)
# rectangle=cv2.rectangle(img,(50,50),(250,350),255,20)
# circle=cv2.circle(img,(250,350),150,255,30)
# ellipse=cv2.ellipse(img,(250,350),(50,200),0,0,360,255,10)

# cv2.imshow("rectangle",rectangle)
cv2.imshow("text",text)
cv2.waitKey(0)
cv2.destroyAllWindows()