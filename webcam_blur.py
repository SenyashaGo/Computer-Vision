import cv2


def blur_face(img):
    (h, w) = img.shape[:2]
    dW = int(w / 3.0)
    dH = int(h / 3.0)
    if dW%2 == 0:
        dW -= 1
    if dH%2 == 0:
        dH -= 1

    return cv2.GaussianBlur(img, (dW, dH), 0)
    

capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
while True:
    ret, img = capture.read()
    if ret:
        faces = face_cascade.detectMultiScale(img, 1.1, 10)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            img[y:y+h, x: x+w] = blur_face(img[y:y+h, x: x+w])
        k = cv2.waitKey(30) & 0xFF
        cv2.imshow('Camera', img)
        if k == 27:
            break
    else:
        break
