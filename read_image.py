# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 11:44:23 2022

@author: Sophie
"""

import cv2
cv2.namedWindow('ImageWindow') 
img=cv2.imread('media\\piccv.jpg')
cv2.imshow('ImageWindow', img)


#black and white picture
cv2.namedWindow('ImageWindows_Gray',img_g)
img_g=cv2.imread('media\\piccv.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('ImageWindows_Gray', img_g)

cv2.waitKey(0)
cv2.destroyAllWindows()