import cv2
import time
from deteksi_gerakan import deteksi_gerakan
from deteksi_ekspresi import deteksi_ekspresi
from deteksi_suara import start_listening, get_status

frame_skip = 1           
display_scale = 0.7      
last_detect_time = 0
delay_between_detection = 0.4 

start_listening()

cap = cv2.VideoCapture("rtsp://admin123:12345678@192.168.11.86:554/stream2")
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)   

if not cap.isOpened():
    print("❌ Tidak dapat membuka stream video.")
    exit()

RED = (0, 0, 255)
WHITE = (255, 255, 255)

frame_count = 0
fps_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Stream berhenti / tidak dapat membaca frame.")
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue  # skip beberapa frame biar gak lag

    display_frame = cv2.resize(frame, None, fx=display_scale, fy=display_scale)

    if time.time() - last_detect_time > delay_between_detection:
        hasil_gerakan = deteksi_gerakan(display_frame)
        hasil_ekspresi = deteksi_ekspresi(display_frame)
        hasil_suara = get_status()
        last_detect_time = time.time()

    # yolo
    for (x1, y1, x2, y2, label, conf, color) in hasil_gerakan["boxes"]:
        cv2.rectangle(display_frame, (x1, y1), (x2, y2), color, 2)
        text = f"{label} ({conf:.2f})"
        cv2.putText(display_frame, text, (x1, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, WHITE, 2)

    # ekspresi
    for (x, y, w, h, emotion, conf, color) in hasil_ekspresi["boxes"]:
        cv2.rectangle(display_frame, (x, y), (x + w, y + h), color, 2)
        emo_text = f"{emotion} ({conf:.1f})"
        cv2.putText(display_frame, emo_text, (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, WHITE, 2)

    # detect logic
    gerak_bahaya = hasil_gerakan["status"] == "mencurigakan"
    ekspresi_bahaya = hasil_ekspresi["status"] == "tidak_aman"
    suara_bahaya = hasil_suara["deteksi"]

    pelecehan_terdeteksi = sum([gerak_bahaya, ekspresi_bahaya, suara_bahaya]) >= 2

    if pelecehan_terdeteksi:
        cv2.putText(display_frame, "🚨 PELECEHAN TERDETEKSI 🚨", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, RED, 3)

    # subtitle
    teks_audio = f"Audio: {hasil_suara['subtitle']}"
    cv2.putText(display_frame, teks_audio, (20, display_frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, WHITE, 2)

    cv2.imshow("Deteksi Pelecehan Lift", display_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
