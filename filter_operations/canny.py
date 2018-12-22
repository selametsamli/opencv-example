import cv2
import numpy as np



kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_blue = np.array([100, 60, 60])
    high_blue = np.array([140, 255, 255])

    canny = cv2.Canny(frame, 150, 200)

    mask = cv2.inRange(hsv, low_blue, high_blue)
    last_pic = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('orjinal', frame)
    cv2.imshow('canny', canny)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
