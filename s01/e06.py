import numpy as np
import cv2 as cv

img = cv.imread('../jane.jpg')
cv.imshow('Jane', img)

# Faktor pengubah
faktor = np.ones(img.shape, dtype=np.uint8) * 150
cerah = cv.add(img, faktor)
redup = cv.subtract(img, faktor)

cv.imshow('Cerah', cerah)
cv.imshow('Redup', redup)

cv.waitKey()
cv.destroyAllWindows()
