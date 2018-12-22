import cv2
import numpy as np

img = cv2.imread('kose-bulma.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

corner = cv2.goodFeaturesToTrack(gray, 300, 0.01, 10)
corner = np.int0(corner)

for corner in corner:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('Corners', img)
cv2.waitKey(0)
