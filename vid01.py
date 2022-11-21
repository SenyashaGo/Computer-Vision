import cv2

cap = cv2.VideoCapture('IMG_9733.MOV') # capture - запись

while True:
    succsess, img = cap.read() # В переменную succsess у нас будет помещено значение True/False. True - если удалось почитать видео. В img - само изображение
    if succsess:

        cv2.imshow("Result", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break