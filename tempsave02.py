# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 14:21:57 2022

@author: Sophie
"""

import cv2
import numpy

cv2.namedWindow('Color')
cv2.namedWindow('Gray')

canvas = numpy.ones((200,200,3), dtype='uint8')
canvas_g=numpy.ones((200,200,1), dtype='uint8')

canvas[:]=(0,0,255)
canvas_g[:]=0

cv2.imshow('Color', canvas)
cv2.imshow('Gray', canvas_g)

cv2.waitKey(0)
cv2.destroyAllWindows()