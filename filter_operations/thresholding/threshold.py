import cv2

import numpy as np

img = cv2.imread('sayfa.jpg')

ret, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY_INV)

gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

ret, otsu = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('orjinal', img)
cv2.imshow('threshold', threshold)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
