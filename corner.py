import numpy as np
import cv2

img = cv2.imread('original.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray)
e = np.float32(gray)
print(e)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)
print(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('Corner', img)