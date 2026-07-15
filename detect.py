from ultralytics import YOLO
import cv2
from traffic_signal import calculate_signal_time


model = YOLO("yolov8n.pt")


def detect_traffic():

    cap = cv2.VideoCapture("videos/traffic.mp4.mp4")

    counts = {
        "car": 0,
        "motorcycle": 0,
        "bus": 0,
        "truck": 0
    }


    while cap.isOpened():

        success, frame = cap.read()

        if not success:
            break

        results = model(frame)

        for result in results:
            for box in result.boxes:

                cls = int(box.cls[0])
                name = model.names[cls]

                if name in counts:
                    counts[name] += 1


    cap.release()


    total = (
        counts["car"]
        + counts["motorcycle"]
        + counts["bus"]
        + counts["truck"]
    )


    green_time = calculate_signal_time(total)


    if total < 20:
        density = "Low"
    elif total < 50:
        density = "Medium"
    else:
        density = "High"


    return {
        "total": total,
        "density": density,
        "green_time": green_time,
        "cars": counts["car"],
        "bikes": counts["motorcycle"],
        "buses": counts["bus"],
        "trucks": counts["truck"]
    }