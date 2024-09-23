import cv2

video_devices = ['/dev/video10', '/dev/video11', '/dev/video12', '/dev/video18', '/dev/video31',
                 '/dev/video13', '/dev/video14', '/dev/video15', '/dev/video16', '/dev/video20',
                 '/dev/video21', '/dev/video22', '/dev/video23', '/dev/video19']

for device in video_devices:
    cap = cv2.VideoCapture(device)
    if cap.isOpened():
        print(f"成功打开摄像头设备 {device}")
        break
    else:
        print(f"无法打开摄像头设备 {device}")
    cap.release()
    