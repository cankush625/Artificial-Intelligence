#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

color = (0, 255, 0)
line_width = 4
radius = 50
point = (0,0)

def drawOnClick(event, x, y, flag, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Pressed ", x, y)
        point = (x, y)

cv2.namedWindow("Streaming")
cv2.setMouseCallback("Streaming", drawOnClick)

while True:
    success, img = cap.read()
    
    # Drawing circle on screen
    cv2.circle(img, point, radius, color, line_width)
    cv2.imshow("Streaming", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

