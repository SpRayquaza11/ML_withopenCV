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
    if len(lmList) != 0:
        print(lmList[4], lmList[8])

        a, b = lmList[4][1], lmList[4][2]
        x, y = lmList[8][1], lmList[8][2]
        c1, c2 = (a + x)//2, (b + y)//2

        cv2.circle(img, (a, b), 12, (255, 255, 255), cv2.FILLED)
        cv2.circle(img, (x, y), 12, (255, 255, 255), cv2.FILLED)
        cv2.circle(img, (c1, c2), 12, (0, 0, 0), cv2.FILLED)

        length = math.hypot(x - a, y - b)
        print(length)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:: {int(fps)}', (30,60), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0))

    cv2.imshow("img", img)
    cv2.waitKey(1)


