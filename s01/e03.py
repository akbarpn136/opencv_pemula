import numpy as np
import cv2 as cv

img = cv.imread('../jane.jpg')
tinggi, lebar = img.shape[:2]

cv.imshow('Jane', img)

# Putar img
Matrix = cv.getRotationMatrix2D((tinggi/2, lebar/2), 45, 1)

putar = cv.warpAffine(img, Matrix, (tinggi, lebar))
cv.imshow('Putar', putar)

cv.waitKey()
cv.destroyAllWindows()
