import cv2
import numpy as np

img = cv2.imread('messi.jpg')
print(str(img.item(100, 100, 1)))  # yeşil rengin pixel değerini verir.
img.itemset((100, 100, 2), 255)  # 100, 100 pixelin ilgili noktasını kırmızı yapar

cv2.imshow('Gorsel', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
