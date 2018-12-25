import cv2
import numpy as np

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('face.xml')

i = 0
person_id = input('ID Bigisi giriniz: ')

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100),
                                      flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        i = i + 1
        cv2.imwrite("face_data/face-" + person_id + "." + str(i) + ".jpg",
                    gray[y:y + h, x:x + w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if i > 19:
            cam.release()
            cv2.destroyAllWindows()
            break
