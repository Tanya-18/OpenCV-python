import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img)
# img[200:300, 100:300] = 255, 0, 0

# cv2.line(img, (0, 0), (300, 300), (0, 254, 0), 3)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)

cv2.circle(img, (450, 50), 35, (255, 0, 255), 4)

cv2.putText(img, "Yep it's me ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (150, 150, 0), 2)

cv2.imshow('image', img)

cv2.waitKey(0)