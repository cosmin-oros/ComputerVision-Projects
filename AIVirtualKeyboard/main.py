import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)




class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.text = text
        self.size = size

    def draw(self, img):
        x, y = self.pos
        w, h =self.size

        cv2.rectangle(img, self.pos, (x+w, y+h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, self.text, (x+20, y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)


buttonList = []

for x in range (0, 5):
    buttonList.append(Button([100*x, 100], "Q"))


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
