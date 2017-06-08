import cv2
import numpy as np
c=cv2.imread("1.jpg")
b=cv2.imread("2.jpg")
x= cv2.addWeighted(c,0.5,b,0.9,0)
cv2.imshow("3.jpg",x)
cv2.waitKey(0)
cv2.destroyAllWindows()