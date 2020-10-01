#!/usr/bin/env python
# coding: utf-8

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:15:20 2020

@author: amogha
"""
#importing neccessary libraries
import cv2
import numpy as np
import copy

def gaussian_(img):
    
    patch=[[1,2,1],[1,4,1],[1,2,1]]
    patch=np.array(patch)

    patch_size=[3,3]
    img_size=img.shape

    output_matrix=np.zeros([img_size[0]-2,img_size[1]-2])

    for i in range(img_size[0]-2):
        for j in range(img_size[1]-2):
            output=np.zeros(patch_size) 
            for k in range(patch_size[0]):
                for l in range(patch_size[1]):
                    output[k,l]=img[i+k,j+l]
            temp=np.sum(patch*output)
            temp=temp/14
            output_matrix[i,j]=temp
    output_matrix=np.uint8(output_matrix)
    
    cv2.imwrite("gaussian.png",output_matrix)
    return output_matrix

def sobel_x(img):
    patch=[[-1,0,1],[-2,0,2],[-1,0,1]]
    patch_size=[3,3]
    img_size=img.shape

    output_matrix=np.zeros([img_size[0]-2,img_size[1]-2])

    for i in range(img_size[0]-2):
        for j in range(img_size[1]-2):
            output=np.zeros(patch_size)
            for k in range(patch_size[0]):
                for l in range(patch_size[1]):
                    output[k,l]=img[i+k,j+l]
            temp=np.sum(patch*output)
            temp=temp/8
            output_matrix[i,j]=temp
        
    cv2.imwrite("sobelx.png",output_matrix)
    return output_matrix

def sobel_y(img):
    patch=[[1,2,1],[0,0,0],[-1,-2,-1]]
    patch=np.array(patch,dtype=np.float32)
    patch_size=[3,3]
    img_size=img.shape

    output_matrix=np.zeros([img_size[0]-2,img_size[1]-2])

    for i in range(img_size[0]-2):
        for j in range(img_size[1]-2):
            output=np.zeros(patch_size)
            for k in range(patch_size[0]):
                for l in range(patch_size[1]):
                    output[k,l]=img[i+k,j+l]
            temp=np.sum(patch*output)
            temp=temp/8
            output_matrix[i,j]=temp
    cv2.imwrite("sobely.png",output_matrix)
    return output_matrix

def non_max_suppression(img,theta):
    img_size=img.shape
    output_matrix=np.zeros((img_size[0],img_size[1]),dtype=np.int32)
    angle=theta*180./np.pi
    angle[angle<0]+=180

    for i in range(1,img_size[0]-1):
            for j in range(1,img_size[1]-1):
                a = 255
                b = 255
                # angle 0
                if (0<=angle[i, j]<22.5) or (157.5<=angle[i,j]<=180):
                    a=img[i,j+1]
                    b=img[i,j-1]
                # angle 45
                elif (22.5<=angle[i,j]<67.5):
                    a=img[i+1,j-1]
                    b=img[i-1,j+1]
                # angle 90
                elif(67.5<=angle[i,j]<112.5):
                    a=img[i+1,j]
                    b=img[i-1,j]
                # angle 135
                elif(112.5<=angle[i,j]<157.5):
                    a = img[i-1,j-1]
                    b = img[i+1,j+1]

                if (img[i,j]>=q) and (img[i,j]>=r):
                    output_matrix[i,j]=img[i,j]
                else:
                    output_matrix[i,j]=0
    return output_matrix
            
def laplacian(img):
    patch_size=[3,3]
    img_s=img.shape
    patch=[[0,1,0],[1,-4,1],[0,1,0]]
    patch=np.array(patch)
    output_m=np.zeros([img_s[0]-2,img_s[1]-2])
    
    for i in range(img_s[0]-2):
        for j in range(img_s[1]-2):
            output=np.zeros(patch_size)
            for k in range(patch_size[0]):
                 for l in range(patch_size[1]):
                    output[k,l]=img[i+k,j+l]
            temp=np.sum(patch*output)
            output_m[i,j]=temp
    return output_m


def hysteresis(img, patch_size):
    img=copy.deepcopy(img)
    size=img.shape
    low=10
    high=30

    for i in range(size[0]-1):
        for j in range(size[1]-1):
            if (img[i,j]<low):
                img[i,j]=0
            elif (img[i,j]>high):
                img[i,j]=255
            else:
                if(img[i,j-1]>high or img[i,j+1]>high or img[i-1,j]>high or img[i+1,j]>high or img[i-1,j-1]>high or img[i-1,j+1]>high or img[i+1,j-1]>high or img[i+1,j+1]>high):
                    img[i,j]=255
                else:
                    img[i,j]=0
    cv2.imwrite('canny_edge_detection_output.png',img)
        
img=cv2.imread("download.jfif",0)
gauss=gaussian_(img)
Ix=sobel_x(gauss)
Iy=sobel_y(gauss)
I=np.hypot(Ix,Iy)
theta = np.arctan2(Iy, Ix)
non_max=non_max_suppression(I,theta)                          
lap=laplacian(non_max)
hysteresis(lap,3)

