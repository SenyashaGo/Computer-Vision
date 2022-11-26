import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image_2022-10-01_13-21-40.jpg")
if(img is not None):
    newimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(newimg, cv2.COLOR_RGB2GRAY)

    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY) # создаст бинарную картинку используя порог, пиксели которые выше 255 - станут белыми, остальные - черными

    # plt.imshow(binary, cmap="gray")
    # plt.show()

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    plt.imshow(img)
    plt.show()