# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:59:40 2016

@author: Lucie
"""

import cv2
import numpy as np

img = cv2.imread('corridor-1.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,50,150,apertureSize = 3)

minLineLength = 100
maxLineGap = 10

lines = cv2.HoughLinesP(edges, 1 ,np.pi/180, 100, minLineLength, maxLineGap)

for x1, y1, x2, y2 in lines[0] :

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('houghlines.jpg',img)
cv2.imshow('Canny Hough',img)
cv2.waitKey(0)
cv2.destroyAllWindows()