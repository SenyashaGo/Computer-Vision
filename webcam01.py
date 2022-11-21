import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 500) # 3 - ширина 
cap.set(4, 300) # 4 - высота

while True:
    success, img = cap.read()
    if success:
        cv2.imshow('Result', img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break
