from ultralytics import YOLO

model = YOLO("models/best.pt")

model.predict(
    source="exemples/",
    conf=0.4,
    save=True,
)
