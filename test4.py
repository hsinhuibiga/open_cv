# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 17:44:27 2022

@author: Sophie
"""

import cv2
import glob
import numpy

cv2.namedWindow('ImageWindow')
#用glob套件把附檔名是jpg的圖片掃描到記憶體裡
data = glob.glob('cropMono\\*.jpg')
data_num = len(data)
#寬 ( 18 +    2  ) *     6    高 35
#寬 (im_w+x_space) * data_num
x_space = 2
img = cv2.imread(data[0])
im_h = img.shape[0]
im_w = img.shape[1]

canvas = numpy.ones((im_h,(im_w+x_space)*data_num,1), 
                      dtype="uint8")
canvas[:]=255

for m,file in enumerate(data):
    g_data = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    for row in range(im_h):
        for col in range(im_w):
            canvas[row][col+(x_space+im_w)*m]=g_data[row][col]

cv2.imshow('ImageWindow',canvas)
cv2.imwrite('media\\merge.jpg',canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()