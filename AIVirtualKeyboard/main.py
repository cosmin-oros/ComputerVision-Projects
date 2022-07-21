import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)


class Button():
    def __init__(self, pos, text, size=[100, 100]):
        self.pos = pos
        self.text = text
        self.size = size

    def draw(self, img):
        x, y = self.pos
        w, h =self.size

        cv2.rectangle(img, self.pos, (x+w, y+h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, self.text, (x+25, y+25), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
        return img


myButton = Button([100, 100], "Q")

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    img = myButton.draw(img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
