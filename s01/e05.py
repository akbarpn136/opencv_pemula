import numpy as np
import cv2 as cv

img = cv.imread('../jane.jpg')
tinggi, lebar = img.shape[:2]
cv.imshow('Jane', img)

# Crop img
cropped = img[25:tinggi-25, 25:lebar-25]
cv.imshow('Perkecil', cropped)

cv.waitKey()
cv.destroyAllWindows()
