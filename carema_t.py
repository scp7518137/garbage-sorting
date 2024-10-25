import cv2

# 选择视频源，0通常是默认的内置或第一个连接的摄像头
cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # 读取一帧图像
    ret, frame = cap.read()

    # 如果正确读取帧，ret将为True
    if not ret:
        print("无法接收帧 (可能已达到视频结尾？)。退出...")
        break

    # 显示结果帧
    cv2.imshow('Camera Feed', frame)

    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 当一切完成后，释放VideoCapture对象
cap.release()
cv2.destroyAllWindows()
