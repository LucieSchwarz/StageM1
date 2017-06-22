# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 10:20:54 2016

@author: Lucie
"""

import cv2


kernel_size = 3
scale = 1
delta = 0
ddepth = cv2.CV_16S

img = cv2.imread('corridor-1.jpg')
img = cv2.GaussianBlur(img,(3,3),0)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray_lap = cv2.Laplacian(gray,ddepth,ksize = kernel_size,scale = scale,delta = delta)
dst = cv2.convertScaleAbs(gray_lap)

cv2.imwrite('laplace.jpg',dst)
cv2.imshow('laplacian',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()