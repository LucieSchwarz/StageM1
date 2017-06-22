# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 15:20:40 2016

@author: Lucie
"""

import cv2
import math


# calcul des angles alpha
def calculAlpha(thetaH, thetaW, height_obj, height_img, width_obj, width_img):
    
    proportionH = height_obj/float(height_img)
    proportionW = width_obj/float(width_img)
    
    alphaH=thetaH*proportionH
    alphaW=thetaW*proportionW
    return math.radians(alphaH), math.radians(alphaW)
 
 
# retourne la profondeur et la hauteur réelle    
def calculDistanceHauteur(alpha1H, alpha1W, alpha2H, alpha2W, d):
    
    tan1H=math.tan(alpha1H)
    tan1W=math.tan(alpha1W)
    
    tan2H=math.tan(alpha2H)
    tan2W=math.tan(alpha2W)
    
    height=d*tan1H*tan2H/(tan2H-tan1H)
    width=d*tan1W*tan2W/(tan2W-tan1W)
    
    profH=height/tan1H
    profW=width/tan1W
    print ("Height : %f \nWidth : %f" % (height, width))
    
    profondeur = (profH+profW)/2
    print ("Profondeur : %f" % (profondeur))
    
    return[height, width, profondeur]
 
   
# retourne les dimension du rectangle et de l'image    
def WHCube(name):

    im = cv2.imread(name)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    #seuillage
    th3 = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

    #contours
    cont, hierarchy = cv2.findContours(th3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(th3, cont, -1, (255,0,0), 1)
    cv2.imshow('contours',th3)
    
    contours = sorted(cont, key = cv2.contourArea, reverse = True)[:10]
    cv2.drawContours(im, contours, -1, (255,0,0), 1)

    i=0
    h=0
    w=0

    for c in contours:
        i=i+1
        if i==1:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            height_img = h
            width_img = w
        if i==2 :
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            height_obj = h
            width_obj = w

    cv2.imshow("rectangle", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return [height_obj, height_img, width_obj, width_img]


# ecrit les dimension du cube dans un fichier    
def WHWrite(h, w, p):
    fichier = open("leNomDuFichier.txt", "w")
    fichier.write("%d\n%d\n%d" % (h,w, p))
    fichier.close()
 
   

thetaH = 37.8 # calculer experimentalement
thetaW = 44.1 # calculer experimentalement

#name1=sys.argv[1]
#name2=sys.argv[2]

name1='ima1.jpg'
name2='ima3.jpg'

d = 3.0 # distance de déplacement du rasp entre les deux prises 

height_obj, height_img, width_obj, width_img = WHCube(name1)
alpha1H, alpha1W = calculAlpha(thetaH, thetaW, height_obj, height_img, width_obj, width_img)

height_obj, height_img, width_obj, width_img = WHCube(name2)
alpha2H, alpha2W = calculAlpha(thetaH, thetaW, height_obj, height_img, width_obj, width_img)

profondeur, height, width = calculDistanceHauteur(alpha1H, alpha1W, alpha2H, alpha2W, d)

WHWrite(height, width, profondeur)

