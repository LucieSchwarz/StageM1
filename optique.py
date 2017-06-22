# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 14:20:48 2016

@author: Lucie
"""

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
    
    
# ecrit les dimension du cube dans un fichier    
def WHWrite(h, w, p):
    fichier = open("leNomDuFichier.txt", "w")
    fichier.write("%d\n%d\n%d" % (h,w, p))
    fichier.close()