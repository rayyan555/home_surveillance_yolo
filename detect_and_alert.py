import cv2
import requests
import tempfile
import os

def send_alert(bot_token, chat_id, frame):
    try:
        _, image_bytes = cv2.imencode(".jpg", frame)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmpfile:
            tmpfile.write(image_bytes.tobytes())
            tmpfile_path = tmpfile.name

        url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
        with open(tmpfile_path, "rb") as photo:
            data = {
                "chat_id": chat_id,
                "caption": "🚨 Alert: Person detected!"
            }
            files = {"photo": photo}
            requests.post(url, data=data, files=files)

        print("[INFO] Alert sent to Telegram.")
        os.remove(tmpfile_path)

    except Exception as e:
        print(f"[ERROR] Could not send alert: {e}")
