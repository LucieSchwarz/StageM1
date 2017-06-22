# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 10:34:19 2016

@author: Lucie
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 15:20:40 2016

@author: Lucie
"""

import lignesFuite as lf
import optique as opt
import sys

thetaH = 37.8 # calculer experimentalement
thetaW = 44.1 # calculer experimentalement

#name1=sys.argv[1]
#name2=sys.argv[2]

name1='ima1.jpg'
name2='ima3.jpg'

d = 3.0 # distance de déplacement du rasp entre les deux prises 


# A FAIRE SUR LES DEUX PHOTOS !!!

#détecter les rectangles

height_img1, width_img1, rect1 = lf.rectangles(name1)
height_img2, width_img2, rect2 = lf.rectangles(name2)

#détecter les points de fuites

points1 = lf.points(name1)
points2 = lf.points(name2)

#récupérer le "bon" rectangle et ses dimensions sur l'image

height_obj1, width_obj1 = lf.goodOne(rect1, points1)
height_obj2, width_obj2 = lf.goodOne(rect2, points2)

#récuperer les dimensions réelles du cube

alpha1H, alpha1W = opt.calculAlpha(thetaH, thetaW, height_obj1, height_img1, width_obj1, width_img1)

alpha2H, alpha2W = opt.calculAlpha(thetaH, thetaW, height_obj2, height_img2, width_obj2, width_img2)

profondeur, height, width = opt.calculDistanceHauteur(alpha1H, alpha1W, alpha2H, alpha2W, d)

#écrire les valeurs dans un fichier

opt.WHWrite(height, width, profondeur)

