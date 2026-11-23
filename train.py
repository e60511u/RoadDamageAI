from ultralytics import YOLO


def main():
    model = YOLO("yolov8n.pt")
    model.train(
        data="C:/Users/Utilisateur/Documents/BUT/SAE/IA/App/dataset/data_rdd2022.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        device=0,
        workers=4,
        patience=15,
        name="rdd2022_n",
    )


if __name__ == "__main__":
    main()
