# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 09:16:06 2016

@author: Lucie
"""

import cv2
import numpy as np

im = cv2.imread('ima1.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#seuillage
#ret,thresh = cv2.threshold(imgray,50,255,0)
th3 = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

#contours
contours, hierarchy = cv2.findContours(th3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(th3, contours, -1, (255,0,0), 1)
cv2.imshow('contours',th3)

#index du plus large contour
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]

#rectangle
x,y,w,h = cv2.boundingRect(cnt)
print "x=%d y=%d w=%d h=%d" %(x, y, w, h)
cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow('rectangle',im)

cv2.waitKey(0)
cv2.destroyAllWindows()
