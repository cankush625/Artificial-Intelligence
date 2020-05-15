#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2
import numpy as np

path = "Downloads/lambo.jpg"
img = cv2.imread(path)

# Scale
# Half sized image
imgHalf = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# Stretched image
imgStretch = cv2.resize(img, (600,600))
# Stretched near image
imgStretchedNear = cv2.resize(img, (600,600), interpolation=cv2.INTER_NEAREST)

# Rotation
matrix = cv2.getRotationMatrix2D((0,0), -20, 1)
imgRotate = cv2.warpAffine(img, matrix, (img.shape[1], img.shape[0]))

cv2.imshow("Half Image", imgHalf)
cv2.imshow("Stretched Image", imgStretch)
cv2.imshow("Stretched Near Image", imgStretchedNear)

cv2.imshow("Rotated Image", imgRotate)

cv2.waitKey(0)
cv2.destroyAllWindows()

