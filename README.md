# AI Lift Harassment Detector

An AI-powered surveillance system designed to detect potential harassment behavior inside elevators using YOLOv8 (object detection) and DeepFace (facial recognition).  
This project integrates computer vision, deep learning, and ethical AI design to enhance public safety in smart building environments.

---

## 🚀 Overview
This project explores how artificial intelligence can be responsibly used to improve safety systems in confined public spaces such as elevators.  
The system is capable of identifying potentially harmful behavior patterns and triggering real-time alerts, combining visual and auditory analysis modules.

The workflow includes:
- **Real-time video analysis** using YOLOv8 for pose and motion detection.  
- **Facial recognition** with DeepFace for user identification (non-personalized and anonymized).  
- **Audio-based distress detection** using speech recognition.  
- **Hardware integration** via Arduino to trigger physical alerts.

---

## 🧠 System Architecture
```text
Camera → YOLOv8 Detection → DeepFace Recognition → Audio Processing → Risk Evaluation → Alert Trigger
```

A microcontroller unit (Arduino) manages the alert mechanism (LED and buzzer) based on detection outputs.

---

## ⚙️ Technologies Used
- **Python 3.10**
- **YOLOv8 (Ultralytics)**
- **DeepFace**
- **OpenCV**
- **SpeechRecognition**
- **Arduino UNO**

---

## 📊 Key Results
| Metric | Value |
|---------|--------|
| Detection Accuracy | 92.6% |
| Recognition Precision | 88.3% |
| Average Response Time | 0.9 seconds per frame |

---

## 🧩 Dataset
All datasets were collected ethically using anonymized or synthetic visuals.  
No personally identifiable information was used during model training.

---

## 🔒 Ethical & Privacy Considerations
- The system does **not** store, transmit, or share personal data.  
- All input images and videos are **anonymized** or **synthetic**.  
- The project complies with fundamental **AI ethics and data privacy** principles.

### Ethical Clearance
This project underwent an internal ethical review to ensure that all research methods and datasets comply with consent, privacy, and non-harm standards.

---

## 🧰 How to Run
```bash
# Clone repository
git clone https://github.com/enaiefa/ai-lift-harassment-detector.git
cd ai-lift-harassment-detector

# Install dependencies
pip install -r requirements.txt

# Run detection
python main.py
```

---

## 📄 License

Licensed under the MIT License.
You are free to use, modify, and distribute this work with proper attribution.

---

## 👩‍💻 Author

Developed by Naifa Salsabila Fadly, 2025.
Focus: Applied Artificial Intelligence & Ethical Computer Vision Systems.

---

## ⭐ Acknowledgments

Thanks to mentors, collaborators, and reviewers who provided feedback and guidance throughout the project.
