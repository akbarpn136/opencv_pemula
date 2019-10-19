import cv2 as cv
from os import walk
from os.path import join

for root, dirs, files in walk('../cat_dog/'):
    if files:
        for file in files:
            img = cv.imread(join(root, file))
            img = cv.resize(img, (150, 150), interpolation=cv.INTER_AREA)
            cv.imwrite(join(root, file), img)
