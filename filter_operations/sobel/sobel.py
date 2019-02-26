import cv2
import numpy as np

img = cv2.imread('sudokubig.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
cv2.waitKey(0)
