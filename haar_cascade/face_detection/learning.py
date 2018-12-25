import cv2, os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
cascade_path = 'face.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)
path = "face_data"


def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    images = []
    labels = []
    for image_path in image_paths:
        image_pil = Image.open(image_path).convert('L')
        image = np.array(image_pil, 'uint8')
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))
        print(nbr)
        faces = face_cascade.detectMultiScale(image)

        for (x, y, w, h) in faces:
            images.append(((image[y:y + h, x:x + w])))
            labels.append(nbr)
            cv2.imshow("resimler eğitim serisine ekleniyor", image[y:y + h, x:x + w])

        return images, labels


images, labels = get_images_and_labels(path)
cv2.imshow("test", images[0])
cv2.waitKey(1)
recognizer.train(images, np.array(labels))
recognizer.write('traning/trainer.yml')
