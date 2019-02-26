import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    canny = cv2.Canny(frame, 150, 200)
    cv2.imshow('original', frame)
    cv2.imshow('canny', canny)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
