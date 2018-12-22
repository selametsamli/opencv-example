import cv2

cascade_src = 'cars.xml'
video_src = 'video1.avi'

cam = cv2.VideoCapture(video_src)
cars_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = cars_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('araclar', img)
    if cv2.waitKey(1) == 27:
        break
cam.release()
