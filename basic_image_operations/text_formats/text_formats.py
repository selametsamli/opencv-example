import cv2
import numpy as np


def metin_yaz():
    img = np.zeros((640, 720, 3), np.uint8)
    img.fill(255)  # içi komple beyaz olur.

    font_scale = 1.0
    color = (0, 0, 255)

    font_face = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, 'FONT_HERSHEY_COMPLEX', (25, 40), font_face, font_scale, color)

    font_face = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(img, 'FONT_HERSHEY_COMPLEX_SMALL', (25, 80), font_face, font_scale, color)

    font_face = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img, 'FONT_HERSHEY_DUPLEX', (25, 120), font_face, font_scale, color)

    font_face = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img, 'FONT_HERSHEY_PLAN', (25, 160), font_face, font_scale, color)

    font_face = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(img, 'FONT_HERSHEY_SCRIPT_COMPLEX', (25, 200), font_face, font_scale, color)

    font_face = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(img, 'FONT_HERSHEY_SCRIPT_SIMPLEX', (25, 240), font_face, font_scale, color)

    font_face = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'FONT_HERSHEY_SIMPLEX', (25, 280), font_face, font_scale, color)

    font_face = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(img, 'FONT_HERSHEY_TRIPLEX', (25, 320), font_face, font_scale, color)

    font_face = cv2.FONT_ITALIC
    cv2.putText(img, 'FONT_ITALIC', (25, 360), font_face, font_scale, color)

    cv2.imshow('text ornekler', img)
    cv2.imwrite('text_ornekler.jpg', img)
    cv2.waitKey(0)


metin_yaz()
