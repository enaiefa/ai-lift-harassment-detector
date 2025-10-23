# deteksi_gerakan.py
from ultralytics import YOLO

model = YOLO("dataset/runs/detect/train/weights/best.pt") 
conf_threshold = 0.5  

def deteksi_gerakan(frame):
    """
    Input: frame (OpenCV image)
    Output: dict { 'status', 'confidence', 'boxes': [(x1,y1,x2,y2,label)] }
    """
    results = model(frame)
    boxes_out = []

    status = "tidak_terdeteksi"

    for box in results[0].boxes:
        conf = float(box.conf[0])
        if conf < conf_threshold:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]

        if cls_name.lower() == "normal":
            status = "normal"
            color = (0, 255, 0)
        else:
            status = "mencurigakan"
            color = (0, 0, 255)

        boxes_out.append((x1, y1, x2, y2, cls_name, conf, color))

    return {"status": status, "confidence": conf if boxes_out else 0.0, "boxes": boxes_out}
