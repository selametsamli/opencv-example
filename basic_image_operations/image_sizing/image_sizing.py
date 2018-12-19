import cv2

img = cv2.imread('cicek.png')
ekran_cozunulurluk = 1280, 720

skala_genislik = ekran_cozunulurluk[0] / img.shape[1]
skala_yukseklik = ekran_cozunulurluk[1] / img.shape[0]
skala = min(skala_genislik, skala_yukseklik)

pencere_genislik = int(img.shape[1] * skala)
pencere_yukseklik = int(img.shape[0] * skala)

cv2.namedWindow('Boyutlanabilir Pencere', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Boyutlanabilir Pencere', pencere_genislik, pencere_yukseklik)

cv2.imshow('Boyutlanabilir Pencere', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
