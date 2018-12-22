import cv2
import numpy as np

img = cv2.imread('saat.jpg')

cv2.imshow('Saat', img)



print(img)


img[80, 80] = [255, 255, 255]

cv2.rectangle(img, (100, 30), (200, 120), (0, 255, 255), 2)
cv2.imshow('rectangle', img)

bolge = img[30:120, 100:200]
img[30:120, 100:200] = [255, 0, 255]
cv2.imshow('boyama', img)

cv2.imshow('bolge', bolge)
cv2.waitKey(0)
cv2.destroyAllWindows()
