import cv2
from cv2 import COLOR_BGR2GRAY
import numpy as np

faceCascade = cv2.CascadeClassifier("../Resources/haarcascade_frontalface_default.xml")
img = cv2.imread('../Resources/lena.png')

imgGray = cv2.cvtColor(img, COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("result", img)
cv2.waitKey(0)
