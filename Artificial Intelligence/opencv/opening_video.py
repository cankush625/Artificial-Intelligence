#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2


# In[41]:


# Reading video
cap = cv2.VideoCapture("Main_Teri_Ho_Gayi__Lyrical_Lyrics_–_Millind_Gaba_Ft_Aditi_Budhathoki____Late.mp4")


# In[42]:


while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    # Adding a delay and if keyboard key "Q" is pressed then break
    if cv2.waitKey(15) & 0xFF ==ord('q'):
        break
        
cv2.destroyAllWindows()
cap.release()

