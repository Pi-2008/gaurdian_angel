"""
Live webcam tracker.

- First time a person is seen  -> full frame saved to  travellers/id_<ID>_time_<TIMESTAMP>.jpg
- First time a knife is seen   -> full frame saved to  dangerous/id_<ID>_time_<TIMESTAMP>.jpg
- Someone staying on screen is NOT saved again.
- If they leave and come back, the tracker gives them a new ID and a new image is saved.

Install:  pip install ultralytics opencv-python
Run:      python traveller_tracker.py      (press q to quit)
"""

import os
from datetime import datetime

import cv2
from ultralytics import YOLO

PERSON_CLASS = 0   # COCO class id for "person"
KNIFE_CLASS = 43   # COCO class id for "knife"

TRAVELLERS_DIR = "travellers"
DANGEROUS_DIR = "dangerous"
os.makedirs(TRAVELLERS_DIR, exist_ok=True)
os.makedirs(DANGEROUS_DIR, exist_ok=True)

model = YOLO("yolov8n.pt")  # downloads automatically on first run
cap = cv2.VideoCapture(0)   # 0 = default webcam (or put a video file path / RTSP url here)

saved_ids = set()  # track IDs we've already saved an image for

while True:
    ok, frame = cap.read()
    if not ok:
        break

    # Track people + knives; persist=True keeps IDs consistent between frames
    result = model.track(
        frame,
        persist=True,
        classes=[PERSON_CLASS, KNIFE_CLASS],
        conf=0.4,
        verbose=False,
    )[0]

    if result.boxes.id is not None:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        ids = result.boxes.id.int().tolist()
        classes = result.boxes.cls.int().tolist()

        for track_id, cls in zip(ids, classes):
            if track_id in saved_ids:
                continue  # already saved while they've been on screen

            saved_ids.add(track_id)
            folder = TRAVELLERS_DIR if cls == PERSON_CLASS else DANGEROUS_DIR
            filename = f"id_{track_id}_time_{timestamp}.jpg"
            cv2.imwrite(os.path.join(folder, filename), frame)  # raw, un-annotated frame
            print(f"Saved {folder}/{filename}")

    cv2.imshow("Live", result.plot())  # preview with boxes and IDs drawn
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
