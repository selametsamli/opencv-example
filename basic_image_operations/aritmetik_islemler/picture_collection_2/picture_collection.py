import cv2

import numpy as np

img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('logo.jpg')

satir, sutun, kanal = img2.shape
roi = img1[0:satir, 0:sutun]  # görselin yapıştırılacağı yer

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)  # 10 dan büyük değerleri al
cv2.imshow('mask', mask)  # siyah renk hariç büyük olanları beyaz yap
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img2gray', img2gray)

im1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('im1_bg', im1_bg)

img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
cv2.imshow('img2_fg', img2_fg)

son_resim = cv2.add(im1_bg, img2_fg)
img1[0:satir, 0:sutun] = son_resim

cv2.imshow('son resim',img1)

cv2.waitKey(0)

