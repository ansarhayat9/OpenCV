import cv2
video=cv2.VideoCapture("videoName")
while (video.isOpened()):
    _,frame=video.read()
    cv2.imshow("video",frame)
    cv2.waitKey(10)
    