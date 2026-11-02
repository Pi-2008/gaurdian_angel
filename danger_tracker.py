"""
Live webcam tracker.

- First time a person is seen  -> full frame saved to  travellers/id_<ID>_time_<TIMESTAMP>.jpg
- First time a knife is seen   -> full frame saved to  dangerous/id_<ID>_time_<TIMESTAMP>.jpg
- Someone staying on screen is NOT saved again.
- If they leave and come back, the tracker gives them a new ID and a new image is saved.

Install:  pip install ultralytics opencv-python lapx
Run:      python traveller_tracker.py      (press q to quit)
"""

import os
import time
from datetime import datetime

import cv2
from ultralytics import YOLO

# ---------------- Settings you can tweak ----------------
MODEL_NAME = "yolov8m.pt"   # bigger model = better at spotting knives (use yolov8l.pt for even better)
IMAGE_SIZE = 960            # larger = better for small objects, but slower
PERSON_MIN_CONF = 0.40      # confidence needed to save a person
KNIFE_MIN_CONF = 0.15       # low on purpose so knives are picked up more easily
KNIFE_COOLDOWN = 5          # seconds to wait before saving another knife image
CAMERA_SOURCE = 0           # 0 = default webcam (or a video file path / stream URL)
# ---------------------------------------------------------

PERSON_CLASS = 0   # COCO class id for "person"
KNIFE_CLASS = 43   # COCO class id for "knife"

TRAVELLERS_DIR = "travellers"
DANGEROUS_DIR = "dangerous"
os.makedirs(TRAVELLERS_DIR, exist_ok=True)
os.makedirs(DANGEROUS_DIR, exist_ok=True)

# Default tracker ignores low-confidence detections, so knives would never get an ID.
# This writes a custom tracker config that accepts them.
TRACKER_FILE = "low_conf_bytetrack.yaml"
if not os.path.exists(TRACKER_FILE):
    with open(TRACKER_FILE, "w") as f:
        f.write(
            "tracker_type: bytetrack\n"
            f"track_high_thresh: {KNIFE_MIN_CONF}\n"
            "track_low_thresh: 0.1\n"
            f"new_track_thresh: {KNIFE_MIN_CONF}\n"
            "track_buffer: 30\n"
            "match_thresh: 0.8\n"
            "fuse_score: True\n"
        )

model = YOLO(MODEL_NAME)
cap = cv2.VideoCapture(CAMERA_SOURCE)

saved_ids = set()       # track IDs we've already saved an image for
last_knife_save = 0.0   # time of the last knife image

while True:
    ok, frame = cap.read()
    if not ok:
        break

    result = model.track(
        frame,
        persist=True,
        classes=[PERSON_CLASS, KNIFE_CLASS],
        conf=KNIFE_MIN_CONF,
        imgsz=IMAGE_SIZE,
        tracker=TRACKER_FILE,
        verbose=False,
    )[0]

    if result.boxes.id is not None:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        ids = result.boxes.id.int().tolist()
        classes = result.boxes.cls.int().tolist()
        confs = result.boxes.conf.tolist()

        for track_id, cls, conf in zip(ids, classes, confs):
            if track_id in saved_ids:
                continue  # already saved while they've been on screen

            if cls == PERSON_CLASS:
                if conf < PERSON_MIN_CONF:
                    continue
                folder = TRAVELLERS_DIR
            else:
                now = time.time()
                if now - last_knife_save < KNIFE_COOLDOWN:
                    continue
                last_knife_save = now
                folder = DANGEROUS_DIR

            saved_ids.add(track_id)
            filename = f"id_{track_id}_time_{timestamp}.jpg"
            cv2.imwrite(os.path.join(folder, filename), frame)  # raw, un-annotated frame
            print(f"Saved {folder}/{filename}")

    cv2.imshow("Live", result.plot())  # preview with boxes and IDs drawn
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
