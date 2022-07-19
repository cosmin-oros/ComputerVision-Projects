import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
# width
cap.set(3, 1280)
# height
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)


