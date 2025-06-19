from surveillance import SurveillanceSystem

if __name__ == "__main__":
    TELEGRAM_TOKEN = "7580133313:AAF9eq_pXqYfUaYJlwDbIr27MD4J7dX2IcI"
    TELEGRAM_CHAT_ID = "7654037862"
    VIDEO_PATH = "D:\\Home Automated Surveillance System\\home_surveillance_yolo\\security_video.mp4"

    system = SurveillanceSystem(telegram_token=TELEGRAM_TOKEN, chat_id=TELEGRAM_CHAT_ID, video_source=VIDEO_PATH)
    system.run()
