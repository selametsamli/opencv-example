import cv2

kamera = cv2.VideoCapture(0)
while True:
    ret, goruntu = kamera.read()
    gri_ton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Goruntu', goruntu)
    cv2.imshow('Gri Ton', gri_ton)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
