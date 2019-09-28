import numpy as np
import cv2 as cv


# membuat latar hitam
hitam = np.zeros((512, 512, 3), dtype=np.uint8)

# membuat garis
cv.line(hitam, (0, 0), (512, 512), (0, 169, 238), 15)

# membuat kotak
cv.rectangle(hitam, (0, 0), (512, 512), (69, 0, 223), 25)

# membuat lingkaran
cv.circle(hitam, (256, 256), 128, (166, 168, 0), -1)

# membuat teks
cv.putText(hitam, 'OpenCV', (200, 260), cv.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

cv.imshow("Hitam", hitam)

cv.waitKey()
cv.destroyAllWindows()
