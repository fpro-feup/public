import cv2
import numpy as np

# https://en.wikipedia.org/wiki/Foreground_detection

cap = cv2.VideoCapture(0)

_, background = cap.read()
beach = cv2.imread('beach.jpg')

while True:
    _, frame = cap.read()

    mask = np.abs(np.mean(frame, 2) - np.mean(background, 2)) > 18
    #mask = np.any(np.abs(frame - background) > 200, 2)
    mask = mask[:, :, np.newaxis]
    img = frame*mask + beach*(1-mask)

    cv2.imshow('frame', img.astype(np.uint8))
    if cv2.waitKey(1) == 27:  # escape
        break

cap.release()
cv2.destroyAllWindows()
