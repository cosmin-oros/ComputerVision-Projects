import cv2

cap = cv2.VideoCapture('video.mp4')
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('reversed2.avi', fourcc, fps, (int(width * 0.5), int(height * 0.5)))

print("Nr of frames are: {}".format(frames))
print("FPS is: {}".format(fps))

frame_index = frames - 1

if cap.isOpened():
    while frame_index != 0:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        frame = cv2.resize(frame, (int(width * 0.5), int(height * 0.5)))
        out.write(frame)
        frame_index -= 1
        if frame_index % 100 == 0:
            print(frame_index)

out.release()
cap.release()
cv2.destroyAllWindows()
