#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[10]:


# Reading image
img = cv2.imread("docker_logo.png")


# In[15]:


# Displaying image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[17]:


# Resizing image
imgResize = cv2.resize(img, (640, 480))
cv2.imshow("Resized Image", imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[18]:


# Cropping an image
imgCrop = img[0:200, 200:600]
cv2.imshow("Cropped Image", imgCrop)
cv2.waitKey(0)
cv2.destroyAllWindows()

