# -*- coding: utf-8 -*-
import cv2

FILENAME = 'Image/Cheon.png'
src = cv2.imread(FILENAME, cv2.IMREAD_COLOR)
height, width, channel = src.shape

dst = cv2.pyrUp(src, dstsize=(width*2, height*2), borderType=cv2.BORDER_DEFAULT);
#dst2 = cv2.pyrDown(src);
dst2 = cv2.pyrUp(dst, dstsize=(width*4, height*4), borderType=cv2.BORDER_DEFAULT);

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()