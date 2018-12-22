import cv2
import numpy as np

img = cv2.imread('kalabalik.jpg')

face_casc = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_casc.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow('yuzler',img)
cv2.waitKey(0)

