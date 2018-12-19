import cv2
import numpy as np

img = cv2.imread('messi.jpg')

ROI = img[310:390, 272:330]

img[310:390, 172:230] = ROI

cv2.imshow('Gorsel', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
