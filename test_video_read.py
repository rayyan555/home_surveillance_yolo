import cv2

video_path = "D:\\Home Automated Surveillance System\\home_surveillance_yolo\\security_video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("[ERROR] Cannot open video file.")
else:
    print("[SUCCESS] Video file opened.")
    ret, frame = cap.read()
    if ret:
        print("[SUCCESS] Frame read successfully.")
        cv2.imshow("Test Frame", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("[ERROR] Failed to read frame.")

cap.release()
