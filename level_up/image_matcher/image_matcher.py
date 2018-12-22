import cv2
import numpy as np
import matplotlib.pyplot as plt

img_big = cv2.imread('buyuk-resim.JPG', 0)
img_small = cv2.imread('kucuk-resim.JPG', 0)

orb = cv2.ORB_create()
key_1, target_1 = orb.detectAndCompute(img_small, None)
key_2, target_2 = orb.detectAndCompute(img_big, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matchers = bf.match(target_1, target_2)
matchers = sorted(matchers, key=lambda x: x.distance)
last_img = cv2.drawMatches(img_big, key_1, img_small, key_2, matchers[:10], None, flags=2)
plt.imshow(last_img)
plt.show()
