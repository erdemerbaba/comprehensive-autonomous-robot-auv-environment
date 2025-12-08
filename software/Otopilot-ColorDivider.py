# -*- coding: utf-8 -*-

import cv2
import numpy as np

def nothing(x):
    pass
#if you can find the spesific color in pic
#pls erase cap,_frame,cap.release and delete # which in frame
#cap=cv2.VideoCapture(0)
cv2.namedWindow("cv")
#example:LH=lower Hue, LS=lower saturation, LV=lower saturation
cv2.createTrackbar("LH","cv",0,255,nothing)
cv2.createTrackbar("LS","cv",0,255,nothing)
cv2.createTrackbar("LV","cv",0,255,nothing)
cv2.createTrackbar("UH","cv",255,255,nothing)
cv2.createTrackbar("US","cv",255,255,nothing)
cv2.createTrackbar("UV","cv",255,255,nothing)
while(1):
    frame=cv2.imread("balls.png")
    #_,frame=cap.read()
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lh=cv2.getTrackbarPos("LH","cv")
    ls=cv2.getTrackbarPos("LS","cv")
    lv=cv2.getTrackbarPos("LV","cv")
    uh=cv2.getTrackbarPos("UH","cv")
    us=cv2.getTrackbarPos("US","cv")
    uv=cv2.getTrackbarPos("UV","cv")
    lb=np.array([lh,ls,lv])
    ub=np.array([uh,us,uv])
    
    mask=cv2.inRange(hsv,lb,ub)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    
    key=cv2.waitKey(1)
    if key==27:
        break

#cap.release()
cv2.destroyAllWindows()

