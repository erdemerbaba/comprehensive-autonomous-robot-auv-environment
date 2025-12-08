# -*- coding: utf-8 -*-

import cv2

cv2.namedWindow("eye")
cam = cv2.VideoCapture(0)

if cam.isOpened(): 
   non, frame = cam.read()
else:
   non = False

while True :
   non, frame = cam.read()
   frameblur = cv2.medianBlur(frame,15)
   framegray = cv2.cvtColor(frameblur, cv2.COLOR_RGB2GRAY)
   circles = cv2.HoughCircles(framegray,cv2.HOUGH_GRADIENT,1,120,param1=100,
                              param2=30,minRadius=20,maxRadius=200)
   if circles is None:
       cv2.imshow("eye", frame)
       continue
   for i in circles[0,:]:
      print (i)
      cv2.circle(frame,(i[0],i[1]),int(i[2]),(0,255,0),1) # draw the outer circle
      cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)# draw the center of circle
   cv2.imshow("eye", frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cam.release()
cv2.destroyWindow("eye")
