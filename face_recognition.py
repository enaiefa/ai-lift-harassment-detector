# deteksi_ekspresi.py
from deepface import DeepFace

uncomfortable = ["angry", "disgust", "fear", "sad"]

def deteksi_ekspresi(frame):
    """
    Output: dict { 'status', 'emotion', 'confidence', 'boxes': [(x,y,w,h,emotion,conf,color)] }
    """
    try:
        results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        if isinstance(results, list):
            faces = results
        else:
            faces = [results]

        boxes_out = []
        final_status = "normal"

        for face in faces:
            x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']
            emotion = face['dominant_emotion']
            confidence = face['emotion'][emotion]

            if emotion in uncomfortable:
                status = "tidak_aman"
                color = (0, 0, 255)
                final_status = "tidak_aman"
            else:
                status = "normal"
                color = (0, 255, 0)

            boxes_out.append((x, y, w, h, emotion, confidence, color))

        return {"status": final_status, "emotion": emotion, "confidence": confidence, "boxes": boxes_out}

    except:
        return {"status": "tidak_terdeteksi", "emotion": None, "confidence": 0.0, "boxes": []}
