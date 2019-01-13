# -*- coding: utf-8 -*-
import numpy as np
import cv2

def showImage():
    FILENAME = 'D:/Work/Python/Image/Test.jpg'
    image = cv2.imread(FILENAME, cv2.IMREAD_UNCHANGED)
    height, width, channel = image.shape
    print(height, width, channel)
    cv2.namedWindow('Test', cv2.WINDOW_NORMAL)
    cv2.imshow('Test', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage()