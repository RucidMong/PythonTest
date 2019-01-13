# -*- coding: utf-8 -*-
import cv2

FILENAME = 'Image/Cheon.png'
src = cv2.imread(FILENAME, cv2.IMREAD_COLOR)
height, width, channel = src.shape

#dst = cv2.blur(src, (9,9), anchor=(-1,-1), borderType=cv2.BORDER_DEFAULT)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(src, 50, 255)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)

cv2.imshow("src", src)
cv2.imshow("canny", canny)
cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
 