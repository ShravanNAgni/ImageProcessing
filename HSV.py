import cv2
import numpy as np

cap= cv2.VideoCapture(0)
while True:
    i, frame= cap.read()
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([10,20,55])
    upper = np.array([255, 255, 255])
    mask=cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    k= cv2.waitKey(0) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
