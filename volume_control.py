import numpy as np
import handtrackingmodule as hm
import time
import cv2
import math

wCam, hCam = 1980, 1080

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)


while True:
    success, img = cap.read()
    cv2.imshow("Img", img)
    cv2.waitKey(1)


