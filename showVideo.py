# -*- coding: utf-8 -*-
import numpy as np
import cv2

def showVideo():
    FILENAME = 'Video/Test.mp4'
    capture = cv2.VideoCapture(FILENAME)
    while True:
        if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
            capture.open(FILENAME)
        ret, frame = capture.read()
        cv2.imshow("TestVideo", frame)

        print(cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FRAME_COUNT)

        if cv2.waitKey(33) > 0: break

    capture.release()
    cv2.destroyAllWindows()

showVideo()