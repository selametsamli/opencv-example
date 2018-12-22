# Notlar:


* img.item( 100, 100, 1 )  ->   mavi: 0 yeşil:1 kırmızı:2
* img.shape() -> yükseklik, genişlik, kanal sayısı
* img.size() -> pixel sayısını verir.
* ROI = img[Ybas:Ybit,Xbas,Ybit] 
* img[:,:,0] -> Mavi
* img[:,:,1] -> Yeşil
* img[:,:,2] -> Kırmızı

---
* img[ 80,80 ] -> 80 e 80 pixelindeki değer nedir [20,24,35]
---

ret, thresh1 = cv2.threshold(img, 127, 255) -> 127 den yukarısını alır

cv2.erode(mask, kernel, iterations=1) -> Gürültüleri azaltır.
cv2.dilate(mask, kernel, iterations=1) -> Gürültüleri arttırır. 

cv2.MORPH_OPEN -> istediğimiz renk dışında renk varsa bu rengi daha da belirginleştirir.
cv2.MORPH_CLOSE -> istediğimiz renk dışında renk varsa bu rengin görünürlüğünü azaltır.
