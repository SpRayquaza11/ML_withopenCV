import numpy as np
import handtrackingmodule as hm
import time
import cv2
import math

wCam, hCam = 1980, 1080

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = hm.handDetector()


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    print(lmList)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:: {int(fps)}', (30,60), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0))

    cv2.imshow("img", img)
    cv2.waitKey(1)


