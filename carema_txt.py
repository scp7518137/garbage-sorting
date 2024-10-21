import cv2

i = 0
while 1:
    device = f'/dev/video{i}'

    cap = cv2.VideoCapture(device)
    if cap.isOpened():
        print(f"成功打开摄像头设备 {device}")
        break
    else:
        print(f"无法打开摄像头设备 {device}")
        i = i + 1
    cap.release()
