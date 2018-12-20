import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_blue = np.array([100, 60, 60])
    high_blue = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, low_blue, high_blue)
    last_pic = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15, 15), np.float32) / 255
    smoothed = cv2.filter2D(last_pic, -1, kernel)

    blur = cv2.GaussianBlur(last_pic, (15, 15), 0)

    median = cv2.medianBlur(last_pic, 15)
    bileteral = cv2.bilateralFilter(last_pic, 15, 75, 75)

    cv2.imshow('orjinal', frame)
    cv2.imshow('son_resim', last_pic)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bileteral', bileteral)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
