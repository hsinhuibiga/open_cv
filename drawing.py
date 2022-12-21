# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 14:46:04 2022

@author: Sophie
"""

import cv2
import numpy


cv2.namedWindow('ImageWindow')
img=cv2.imread('media\\001.jpg')

cv2.line(img,(50,50),(250,50),(255,0,0),2)

cv2.line(img,(50,100),(120,150),(255,0,0),2)
cv2.rectangle(img,(50,100),(250,150),(255,0,0),2)
cv2.rectangle(img,(140,100),(250,150),(0,255,0),-1)

cv2.circle(img,(70,250),50,(50,50,50),3)
cv2.circle(img,(200,250),50,(50,50,50),-1)

points=numpy.array([[350,200],[400,300],[350,300]],numpy.int32)
points_2=numpy.array([[400,200],[450,300],[400,300]],numpy.int32)
points_3=numpy.array([[450,200],[500,300],[450,300]],numpy.int32)
cv2.polylines(img,[points],True,(0,0,0),2)
cv2.polylines(img,[points_2],False,(0,0,0),2)
cv2.fillPoly(img,[points_3],(0,0,0))
cv2.putText(img, "Test text!!", (400,350),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)


cv2.imshow('ImageWindow', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
