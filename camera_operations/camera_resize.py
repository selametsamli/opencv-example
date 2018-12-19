import cv2

kamera = cv2.VideoCapture(0)
# kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

while True:
    ret, goruntu = kamera.read()
    ret = kamera.set(3, 320)  # WIDTH
    ret = kamera.set(4, 320)  # HEIGHT
    cv2.imshow('Goruntu', goruntu)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
