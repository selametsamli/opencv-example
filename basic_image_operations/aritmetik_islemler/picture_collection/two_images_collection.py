import cv2
import numpy as np

x = np.uint8([250])  # 0-255 değerleri alır
y = np.uint8([10])  # toplam 256 ya göre mod alıp toplama işlemi gerçekleştirir.

# print(x + y)
# print(cv2.add(x, y))

img1 = cv2.imread('resim.jpg')
img2 = cv2.imread('logo.jpg')

# toplam = cv2.add(img1, img2)
toplam = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)  # %80 img1 %20 img2 son parametre konum

cv2.imshow('toplam', toplam)
cv2.waitKey(0)
