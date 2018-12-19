import cv2

import numpy as np

img = np.zeros((400, 400, 3), dtype='uint8')  # 400 e 400 siyah birşey oluşturduk
cv2.imshow('siyah', img)

cv2.rectangle(img, (10, 10), (400, 200), (0, 0, 255), 3)
cv2.line(img, (0, 0), (400, 200), (0, 255, 0), 3)
cv2.line(img, (10, 230), (390, 230), (123, 45, 73), 3)
cv2.circle(img, (200, 350), 25, (148, 0, 4), 3)

cv2.putText(img, 'Selam Sürtükler', (5, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 255, 255), 4, cv2.LINE_4)

cv2.imshow('rectangle', img)

cv2.waitKey(0)
