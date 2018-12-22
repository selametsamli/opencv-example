import cv2

cam = cv2.VideoCapture('video.mp4')

human_cascade = cv2.CascadeClassifier('haarcascade-fullbody.xml')

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    human = human_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in human:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 3)

    cv2.imshow('humans', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
