import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi.jpg', 0)
kenarlar = cv2.Canny(img, 300, 600)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('orjinal'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(kenarlar, cmap='gray')
plt.title('kenarlar'), plt.xticks([]), plt.yticks([])
plt.show()
