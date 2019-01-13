# -*- coding: utf-8 -*-
import cv2

FILENAME = 'Image/Cheon.png'
src = cv2.imread(FILENAME, cv2.IMREAD_COLOR)
height, width, channel = src.shape

#dst = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("src", src)
cv2.imshow("gray", gray)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()