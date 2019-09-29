import numpy as np
import cv2 as cv

img = cv.imread('../jane.jpg')

cv.imshow('Jane', img)

# Perbesar img
skala = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_LANCZOS4)
cv.imshow('Perbesar Img', skala)

# Perkecil img
perkecil = cv.resize(img, None, fx=0.6, fy=0.6, interpolation=cv.INTER_AREA)
cv.imshow('Perkecil', perkecil)

cv.waitKey()
cv.destroyAllWindows()
