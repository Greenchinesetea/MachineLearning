import numpy as haha
import cv2
vid = cv2.VideoCapture("E:/w.mp4")
while vid.isOpened():
    brr,frame = vid.read()
    cv2.imshow("winname", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    
vid.release()
cv2.destroyAllWindows()
