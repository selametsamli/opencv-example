import cv2
import numpy as np

img = cv2.imread('messi.jpg')

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

img[:, :, 0] = 0  # mavi bileşenleri 0 ladık
img[:, :, 2] = 255 # kırmızı renkleri 255 yaparız

cv2.imshow('Gorsel', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
