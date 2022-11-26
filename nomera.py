import cv2 
import easyocr # позволяет считывать текст с картинки
import imutils # позволяет например, вращать изображение
from matplotlib import pyplot as pl
import numpy as np
img = cv2.imread("e1534001090227.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter, 30, 200)

cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)[:8]

pos = None
for i in cont:
    approx = cv2.approxPolyDP(i, 10, True)
    if len(approx) == 4:
        pos = approx
        break

mask1= np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask1, [pos], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask=mask1)






pl.imshow(cv2.cvtColor(bitwise_img, cv2.COLOR_BGR2RGB))
pl.show()