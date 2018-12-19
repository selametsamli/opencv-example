import cv2
import numpy as np

img = cv2.imread('messi.jpg')
print("Renkli görselin pixel değeri  : ", str(img.size))

img = cv2.imread('messi.jpg', 0)
print("Renksiz görselin pixel değeri : ", str(img.size))

print(str(img.shape))
print(str(len(img.shape)))

if str(len(img.shape)) == 3:
    print("Renklidir.")
else:
    print("Renksizdir.")

cv2.imshow('Gorsel', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
