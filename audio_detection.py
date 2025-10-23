import speech_recognition as sr
import threading
import cv2

subtitle_text = ""
pelecehan_terdeteksi = False
_thread_active = False  

def recognize_speech():
    global subtitle_text, pelecehan_terdeteksi
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio, language="id-ID")
                subtitle_text = text
                print(f"[Suara]: {text}")

                keywords = ["tolong", "help", "jangan", "berhenti", "stop", "awas"]
                pelecehan_terdeteksi = any(kw in text.lower() for kw in keywords)

                if pelecehan_terdeteksi:
                    print("🚨 Pelecehan terdeteksi!")
            except sr.UnknownValueError:
                subtitle_text = "..."
                pelecehan_terdeteksi = False
            except sr.RequestError:
                subtitle_text = "Gagal terhubung ke layanan Google."
                pelecehan_terdeteksi = False
                break

def start_listening():
    """Menjalankan thread pengenalan suara (sekali saja)."""
    global _thread_active
    if not _thread_active:
        t = threading.Thread(target=recognize_speech, daemon=True)
        t.start()
        _thread_active = True
        print("[INFO] Thread pengenalan suara dimulai.")

def get_status():
    """Mengembalikan status deteksi dan teks terbaru."""
    return {
        "subtitle": subtitle_text,
        "deteksi": pelecehan_terdeteksi
    }
