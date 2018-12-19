import cv2

resim = cv2.imread('messi.jpg')
up = cv2.pyrUp(resim)
down = cv2.pyrDown(resim)

cv2.imshow('Orjinal', resim)
cv2.imshow('UP', up)
cv2.imshow('Down', down)
cv2.waitKey(0)
