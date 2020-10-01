#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np 
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("download.jfif",0)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()


# In[ ]:




