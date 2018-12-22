import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade-eye.xml')

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 3)

        roi_gray = gray[y:y + h, x:x + w]
        roi_rgb = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_rgb, (ex, ey), (ex + ew, ey + eh), (255, 0, 255), 3)

    cv2.imshow('goruntu', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
