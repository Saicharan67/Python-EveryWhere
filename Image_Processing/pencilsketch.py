# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:02:09 2020

@author: Rupa-421
"""
import cv2
#imread is used to read an image file 
l=cv2.imread(r'C:\Users\admin\Pictures\harry2.jpg',1)
#resize is used to change the shape of the image
c=cv2.resize(l,(500,500))
img_gray=cv2.cvtColor(c,cv2.COLOR_BGR2GRAY)
#bitwise_not turns a gray colour image little negative
img_invert=cv2.bitwise_not(img_gray)
img_smoothing=cv2.GaussianBlur(img_invert,(21,21),sigmaX=0,sigmaY=0)
z=cv2.divide(img_gray,255-img_smoothing,scale=256)
cv2.imshow('image',z)
cv2.waitKey(0)
cv2.destroyAllWindows()