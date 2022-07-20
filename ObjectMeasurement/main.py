import cv2
import numpy as np
import utils

webcam = True
# path = '' for photos
path = ''
cap = cv2.VideoCapture(0)
cap.set(10, 160)
cap.set(3, 1920)
cap.set(4, 1080)

scale = 3
wP = 210*scale
hP = 297*scale

while True:
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread(path)

    img, finalContours = utils.getContours(img, showCanny=False, minArea=50000, filter=4)

    if len(finalContours) != 0:
        biggest = finalContours[0][2]
        # print(biggest)
        imgWarp = utils.warpImg(img, biggest, wP, hP)

        img2, finalContours2 = utils.getContours(imgWarp, showCanny=False, minArea=2000, filter=4, cThr=[50, 50], draw=False)

        if len(finalContours) != 0:
            for obj in finalContours2:
                cv2.polylines(img2, [obj[2], True, (255, 0, 0), 2])
                nPoints = utils.reorder(obj[2])
                nW = round((utils.findDis(nPoints[0][0]//scale, nPoints[1][0]//scale)/10), 1)
                nH = round((utils.findDis(nPoints[0][0] // scale, nPoints[2][0] // scale)/10), 1)
                cv2.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[0][0][0]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                cv2.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[0][0][0]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                x, y, w, h = obj[3]
                cv2.putText(img2, '{}cm'.format(nW), (x+30, y-10), (255, 0, 255), 2)
                cv2.putText(img2, '{}cm'.format(nH), (x-70, y+h//2), (255, 0, 255), 2)

        cv2.imshow('Warped', img2)

    img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    cv2.imshow('Original', img)
    cv2.waitKey(1)
