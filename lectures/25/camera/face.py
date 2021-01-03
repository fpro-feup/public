import cv2
import numpy as np

RECT = 100
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    min_diff = np.inf

    for row in range(0, frame.shape[0]-RECT, RECT//2):
        for col in range(0, frame.shape[1]-RECT, RECT//2):
            rect = frame[row:row+RECT, col:col+RECT]
            color = rect.mean((0, 1))
            dcolor = np.mean(np.abs(color - np.array((84, 102, 138))))
            if dcolor < min_diff:
                min_diff = dcolor
                pt1 = (col, row)

    pt2 = (pt1[0]+RECT, pt1[1]+RECT)
    frame = cv2.rectangle(frame, pt1, pt2, (255, 0, 0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:  # escape
        break

cap.release()
cv2.destroyAllWindows()
