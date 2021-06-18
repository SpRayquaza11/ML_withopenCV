import cv2
import mediapipe as mp
import time

class handdetector():



mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for iden, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(iden, cx, cy)
                if iden == 0:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (1, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255), 3)
    cv2.imshow("image", img)
    cv2.waitKey(1)

    def main():
        pTime = 0
        cTime = 0
        cap = cv2.VideoCapture(0)
        while True:
            success, img = cap.read()

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime

            cv2.putText(img, str(int(fps)), (1, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255), 3)
            cv2.imshow("image", img)
            cv2.waitKey(1)


    if __name__ =="__main__":
        main()