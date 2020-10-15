# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:02:09 2020

@author: Rupa-421
"""

import cv2
import numpy as np
img=cv2.imread(r'C:\Users\admin\Pictures\building.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_smoothing=cv2.medianBlur(gray,5)
getEdge=cv2.adaptiveThreshold(img_smoothing,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
colorImg=cv2.bilateralFilter(img,9,300,300)
cartoonImg=cv2.bitwise_and(colorImg,colorImg,mask=getEdge)
cv2.imshow("img",cartoonImg)
cv2.waitKey(0)
cv2.destroyAllWindows()