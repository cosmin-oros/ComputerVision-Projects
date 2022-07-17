import math
import cv2
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=1)

class SnakeGameClass:
    def __init__(self):
        # all points of the snake
        self.points = []
        # distance between each point
        self.lengths = []
        # total length of the snake
        self.currentLength = 0
        # total allowed length
        self.allowedLength = 150
        # previous head point
        self.previousHead = 0, 0

    def update(self, imgMain, currentHead):
        px, py = self.previousHead
        cx, cy = currentHead

        self.points.append([cx, cy])
        distance = math.hypot(cx-px, cy-py)
        self.lengths.append(distance)
        self.currentLength += distance
        self.previousHead = cx, cy

        # draw snake
        for i, point in enumerate(self.points):
            if i != 0:
                cv2.line(imgMain, self.points[i-1], point, (0, 255, 255), 20)
        cv2.circle(img, self.points[-1], 20, (200, 0, 200), cv2.FILLED)


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img,flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]

    cv2.imshow("Image",img)
    cv2.waitKey(1)