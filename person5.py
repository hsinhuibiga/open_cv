# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 11:34:28 2022

@author: Sophie
"""

import cv2

cv2.namedWindow('ImageWindow')
img = cv2.imread("media\\person5.jpg")
cv2.imshow('ImageWindow', img)
#cv2.imwrite('media\\img01.jpg', img)

#特徵檔路徑物件 = OpenCV安裝路徑下面的Haar分類器的特徵存放路徑

#                               +OpenCV預設就提供的"正面"人臉辨識權重檔
cas_path = cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
#宣告一個分類器的物件，並且跟他講用哪個權重檔
face_cas = cv2.CascadeClassifier(cas_path)

faces = face_cas.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5,
                                  minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)

print(faces)

# OpenCV回應我們的方式是左上角的(x,y)與w,h
# 擷取臉部圖形及存檔
# 每個人臉截取在temp變數

count = 1
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    temp = img[y:y + h, x:x + w]
    cv2.imwrite('media\\face' + str(count) + '.jpg', temp)
    count = count + 1

cv2.imshow('ImageWindow', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
