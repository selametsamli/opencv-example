import cv2
import numpy as np


cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')

while True:
    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow('orjinal', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cam.release()
