# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 16:57:07 2022

@author: Sophie
"""

import cv2

#找編號0攝影機
camera=cv2.VideoCapture(0)
cv2.namedWindow('Webcam')
while(camera.isOpened()):
    hassingnal, img=camera.read()
    if hassingnal ==True:
        #左右顛倒
        img=cv2.flip(img,1)
        cv2.imshow('Webcam',img)
        #每100秒採樣一次案件，等待時間的效果
        inp=cv2.waitKey(100)
        #以x按鍵停止攝影機
        if inp==ord('x') or inp==ord('x'):
            break
        #以x按鍵拍照截圖並存到media資料夾
        if inp==ord('z') or inp==ord('z'):
            cv2.imwrite('media\\photo.jpg', img)
  
camera.release()
cv2.destroyAllWindows()