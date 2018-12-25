import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('traning/trainer.yml')
cascade_path = "face.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
path = "face_data"
cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for x, y, w, h in faces:
        tahmin_edilen_kisi, conf = recognizer.predict(gray[y:y + h, x:x + w])
        cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2)

        if tahmin_edilen_kisi == 1:
            tahmin_edilen_kisi = "Selamet Şamlı"
        elif tahmin_edilen_kisi == 2:
            tahmin_edilen_kisi = "İlteriş Keskin"
        else:
            tahmin_edilen_kisi = "Bilinmeyen resim."

        font_face = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 255, 255)
        cv2.putText(img, str(tahmin_edilen_kisi), (x, y + h), font_face, font_scale, font_color)
        cv2.imshow("Resim", img)
        cv2.waitKey(10)
