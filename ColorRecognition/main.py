import cv2

# 0 -> first webcam
cap = cv2.VideoCapture(0)

while True:
    # get a frame
    _, frame = cap.read()

    cv2.imshow("Frame", frame)
    cv2.waitKey(0)