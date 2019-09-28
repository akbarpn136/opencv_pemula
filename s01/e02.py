import numpy as np
import cv2 as cv

img = cv.imread('../jane.jpg')
tinggi, lebar = img.shape[:2]

cv.imshow('Jane', img)

# Geser img
Matrix = np.array([
    [1, 0, 25],
    [0, 1, 0]
], dtype=np.float32)

pindah = cv.warpAffine(img, Matrix, (tinggi, lebar))
cv.imshow('Pindah', pindah)

cv.waitKey()
cv.destroyAllWindows()
