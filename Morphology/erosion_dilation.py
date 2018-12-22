import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_red = np.array([150, 30, 30])
    high_red = np.array([190, 255, 255])

    low_blue = np.array([100, 60, 60])
    high_blue = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, low_red, high_red)
    last_pic = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('orjinal', frame)
    cv2.imshow('son_resim', last_pic)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
