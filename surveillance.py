import cv2
from ultralytics import YOLO
from detect_and_alert import send_alert

class SurveillanceSystem:
    def __init__(self, video_source=0, stop_event=None):
        self.model = YOLO("yolov8n.pt")
        self.telegram_token = "7580133313:AAF9eq_pXqYfUaYJlwDbIr27MD4J7dX2IcI"
        self.chat_id = "7654037862"
        self.capture = cv2.VideoCapture(video_source)
        self.stop_event = stop_event

    def run(self, display_window=False):
        print("[INFO] Surveillance started.")

        while True:
            if self.stop_event and self.stop_event.is_set():
                print("[INFO] Stop event received.")
                break

            ret, frame = self.capture.read()
            if not ret:
                print("[INFO] No more frames or camera disconnected.")
                break

            results = self.model(frame)
            alert_triggered = False
            for result in results:
                for box in result.boxes:
                    cls_id = int(box.cls[0])
                    label = self.model.names[cls_id]
                    conf = float(box.conf[0])
                    if label.lower() == "person" and conf > 0.5:
                        print(f"[ALERT] Person detected with {conf:.2f} confidence.")
                        send_alert(self.telegram_token, self.chat_id, frame)
                        alert_triggered = True
                        break
                if alert_triggered:
                    break

            if display_window:
                annotated = results[0].plot()
                cv2.imshow("Surveillance", annotated)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        self.capture.release()
        if display_window:
            cv2.destroyAllWindows()
        print("[INFO] Surveillance ended.")
