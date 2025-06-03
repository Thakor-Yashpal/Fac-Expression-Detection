from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np
import os


model = YOLO("best.pt")
cap = cv2.VideoCapture(0)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % 3 == 0:  # Only predict every 3rd frame
        results = model.predict(source=frame, show=True, verbose=False)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# face\Scripts\activate