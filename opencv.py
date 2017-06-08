import cv2
import numpy as np

def nothing(x):
    pass
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow("Image")
cv2.createTrackbar('b',"Image",0,255,nothing)
cv2.createTrackbar('g',"Image",0,255,nothing)
cv2.createTrackbar('r',"Image",0,255,nothing)
switch='0:OFF \n1:ON'
cv2.createTrackbar(switch,"Image",0,1,nothing)
while(1):
    cv2.imshow("Image",img)
    k=cv2.waitKey(1)& 0xFF
    if k==27:
        break
    R = cv2.getTrackbarPos('r', "Image")
    B = cv2.getTrackbarPos('b', "Image")
    G = cv2.getTrackbarPos('g', "Image")
    S = cv2.getTrackbarPos(switch, "Image")
    if S==0:
        img[:]=0
    else:
        img[:]=[B,G,R]
cv2.destroyAllWindows()
