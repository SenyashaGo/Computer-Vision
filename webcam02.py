import cv2  



capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_fullbody.xml")
while True:
    ret, img = capture.read()
    if ret:
        faces = face_cascade.detectMultiScale(img, 1.1, 10)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=1) # cv2.FILLED - заливка
        k = cv2.waitKey(30) & 0xFF
        cv2.imshow('Camera', img)
        if k == 27:
            break
    else:
        break
