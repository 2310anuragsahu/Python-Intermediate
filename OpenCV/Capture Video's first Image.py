import cv2
import time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

check, frame = video.read()

print(check)
print(frame)

time.sleep(3)

cv2.imshow('Capture', frame)
cv2.waitKey(0)

video.release()
cv2.destroyAllWindows()
