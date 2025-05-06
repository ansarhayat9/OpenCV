import cv2
import os #to save image at different path

# open image as
# Grayscale = flag should be 0
# as it as = flag should be -1
# colored = flag should be 1

img = cv2.imread("image1.jpg")
# cv2.imwrite(os.path.join("D:/ savedimage.png",img))
cv2.imwrite("savedimage.png",img)   # To save

cv2.imshow("image",img)
cv2.waitKey(0)