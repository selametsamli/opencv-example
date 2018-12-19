import cv2
import numpy as np

img = cv2.imread('saat.jpg')

print(img[80, 80])
img[80, 80] = [255, 255, 255]

bolge = img[30:120, 100:200]
img[0:90, 0:100] = bolge

cv2.imshow('Saat', img)
cv2.imshow('bolge', bolge)
cv2.waitKey(0)
cv2.destroyAllWindows()
