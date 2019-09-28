import cv2 as cv

img = cv.imread('jane.jpg', 0)
cv.imshow('Jane', img)

cv.waitKey()
cv.destroyAllWindows()
