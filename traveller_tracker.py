"""
Bus Passenger Manifest Tracker (Guardian Angel)

Monitors the bus door / entrance using YOLOv8:
1. Tracks each person who boards the bus.
2. Assigns a unique persistent ID to each passenger.
3. Saves a full-frame photo and a cropped passenger portrait to 'travellers/'.
4. Logs every boarding passenger to a structured file: 'bus_manifest.csv'.
5. Also detects knives/weapons and logs threats to 'dangerous/' and 'threat_alerts.csv'.

Install:  pip install ultralytics opencv-python lapx
Run:      python traveller_tracker.py   (Press 'q' to quit)
"""

import os
import csv
import time
from datetime import datetime

import cv2
from ultralytics import YOLO

# ----------------- Settings -----------------
MODEL_NAME = "yolov8n.pt"     # Fast lightweight model (use yolov8m.pt for higher accuracy)
CAMERA_SOURCE = 0             # 0 = webcam (or video file: "bus_entry.mp4", or RTSP stream)
PERSON_MIN_CONF = 0.40        # Confidence threshold for passengers
KNIFE_MIN_CONF = 0.25         # Confidence threshold for weapons
PERSON_CLASS = 0              # COCO id for "person"
KNIFE_CLASS = 43              # COCO id for "knife"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRAVELLERS_DIR = os.path.join(BASE_DIR, "travellers")
DANGEROUS_DIR = os.path.join(BASE_DIR, "dangerous")
MANIFEST_FILE = os.path.join(BASE_DIR, "bus_manifest.csv")
THREAT_LOG = os.path.join(BASE_DIR, "threat_alerts.csv")

os.makedirs(TRAVELLERS_DIR, exist_ok=True)
os.makedirs(DANGEROUS_DIR, exist_ok=True)

# Initialize CSV log files with headers if they don't exist
if not os.path.exists(MANIFEST_FILE):
    with open(MANIFEST_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Passenger_ID", "Confidence", "Status", "Full_Frame_File", "Crop_File"])

if not os.path.exists(THREAT_LOG):
    with open(THREAT_LOG, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Threat_ID", "Object_Type", "Confidence", "Image_File"])

print(f"Loading YOLO model ({MODEL_NAME})...")
model = YOLO(MODEL_NAME)

cap = cv2.VideoCapture(CAMERA_SOURCE)
if not cap.isOpened():
    print(f"Error: Unable to open camera source {CAMERA_SOURCE}")
    exit(1)

saved_ids = set()
passenger_counter = 0

print("=" * 60)
print("🚌 BUS PASSENGER MANIFEST TRACKER ACTIVE")
print(f"📁 Saving Passenger Manifest -> {MANIFEST_FILE}")
print(f"📁 Saving Threat Alerts      -> {THREAT_LOG}")
print("Press 'q' in the video window to stop.")
print("=" * 60)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape

    # Track persons and weapons with persistent IDs across frames
    results = model.track(
        frame,
        persist=True,
        classes=[PERSON_CLASS, KNIFE_CLASS],
        conf=0.3,
        verbose=False
    )[0]

    if results.boxes is not None and results.boxes.id is not None:
        boxes = results.boxes.xyxy.int().tolist()
        ids = results.boxes.id.int().tolist()
        classes = results.boxes.cls.int().tolist()
        confs = results.boxes.conf.tolist()
        now_dt = datetime.now()
        timestamp = now_dt.strftime("%Y-%m-%d %H:%M:%S")
        ts_filename = now_dt.strftime("%Y%m%d_%H%M%S")

        for box, track_id, cls, conf in zip(boxes, ids, classes, confs):
            if track_id in saved_ids:
                continue

            x1, y1, x2, y2 = box
            # Ensure coordinates stay within frame bounds
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(w, x2), min(h, y2)

            if cls == PERSON_CLASS and conf >= PERSON_MIN_CONF:
                saved_ids.add(track_id)
                passenger_counter += 1

                # 1. Full frame
                full_name = f"passenger_id_{track_id}_{ts_filename}.jpg"
                full_path = os.path.join(TRAVELLERS_DIR, full_name)
                cv2.imwrite(full_path, frame)

                # 2. Cropped passenger portrait
                crop_name = f"passenger_crop_id_{track_id}_{ts_filename}.jpg"
                crop_path = os.path.join(TRAVELLERS_DIR, crop_name)
                crop_img = frame[y1:y2, x1:x2]
                if crop_img.size > 0:
                    cv2.imwrite(crop_path, crop_img)

                # 3. Log to CSV file
                with open(MANIFEST_FILE, "a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([timestamp, track_id, f"{conf:.2f}", "Boarded Bus", full_name, crop_name])

                print(f"[+] Boarded: Passenger #{passenger_counter} (Track ID: {track_id}) saved to {MANIFEST_FILE}")

            elif cls == KNIFE_CLASS and conf >= KNIFE_MIN_CONF:
                saved_ids.add(track_id)
                threat_name = f"weapon_id_{track_id}_{ts_filename}.jpg"
                threat_path = os.path.join(DANGEROUS_DIR, threat_name)
                cv2.imwrite(threat_path, frame)

                with open(THREAT_LOG, "a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([timestamp, track_id, "Knife/Weapon", f"{conf:.2f}", threat_name])

                print(f"[!] DANGER ALERT: Weapon detected (Track ID: {track_id}) saved to {THREAT_LOG}")

    # Draw stats overlay on live display
    display_frame = results.plot()
    cv2.rectangle(display_frame, (10, 10), (320, 60), (20, 20, 20), -1)
    cv2.putText(
        display_frame,
        f"Passengers Boarded: {passenger_counter}",
        (20, 42),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 120),
        2
    )

    cv2.imshow("Guardian Angel - Bus Passenger Tracker", display_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Tracking completed. Total passengers registered: {passenger_counter}")
print(f"Manifest written to: {MANIFEST_FILE}")
