import cv2
import numpy as np

img = cv2.imread("../Resources/lambo.png")
print(img.shape)

imgResize = cv2.resize(img, (800, 500))

imgCrop = img[0:150, 150:450]

cv2.imshow("image", img)
cv2.imshow("imageRe", imgResize)
cv2.imshow("imageCrop", imgCrop)

cv2.waitKey(0)