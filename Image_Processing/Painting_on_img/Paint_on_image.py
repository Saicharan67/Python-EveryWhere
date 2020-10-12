# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:03:14 2020

@author: Rupa-421
"""
import cv2
import numpy as np
img=cv2.imread(r'C:\Users\admin\Pictures\harry.jpg')
k=cv2.resize(img,(400,400))
j=False
def draw_circle(event,x,y,flags,param):
    global j
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(k,(x,y),100,(751,131,251),-1)
        j=True
    elif event==cv2.EVENT_MOUSEMOVE:
        if j==True:
            cv2.circle(k,(x,y),20,(251,131,75),-1)
    elif event==cv2.EVENT_RBUTTONDOWN:
        j=False
cv2.namedWindow('paint on harry')
cv2.setMouseCallback("paint on harry",draw_circle)
while True:
    cv2.imshow('paint on harry',k)
    if cv2.waitKey(3) & 0xFF==27:
        break
cv2.destroyAllWindows()