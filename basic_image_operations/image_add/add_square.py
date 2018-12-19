import cv2

img = cv2.imread('cicek.png')
cv2.imshow('Orjinal', img)

cv2.rectangle(img, (200, 70), (320, 180), (255, 0, 0), 2)
cv2.imshow('dortgen', img)

cv2.waitKey(0)
