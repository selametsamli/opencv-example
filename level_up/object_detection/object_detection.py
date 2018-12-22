import cv2
import numpy as np

img_rgb = cv2.imread('ana-resim.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

object = cv2.imread('template.jpg', 0)

w, h = object.shape[::-1]

res = cv2.matchTemplate(img_gray, object, cv2.TM_CCOEFF_NORMED)

threshold = 0.8

loc = np.where(res > threshold)  # eşleştirme %80'den büyük ise loc içerisinde tut.

for n in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, n, (n[0] + w, n[1] + h), (0, 255, 255), 2) #bulunan her eşleştirmeyi kare içerisine aldık.

cv2.imshow('bulunan nesneler', img_rgb)
cv2.waitKey(0)