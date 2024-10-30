import cv2

camera_id = 0
cap = cv2.VideoCapture(camera_id)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 500, 500)  # 调节窗口大小
i = 0
if not cap.isOpened():
    print("无法打开摄像头")

while True:
    ret, frame = cap.read()
    if ret:
        height, width, _ = frame.shape
        print(height, width)
        center_x = 640 // 2
        center_y = 480 // 2
        box_size = 50

        start_point = (center_x - box_size, center_y - box_size)
        end_point = (center_x + box_size, center_y + box_size)

        frame = cv2.rectangle(frame, start_point, end_point, color=(0, 255, 0), thickness=1)

        cv2.imshow('image', frame)

        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif cv2.waitKey(1) & 0xFF == ord('w'):
                i = 1
                break
        if i == 1:
            break

    else:
        print("无法获取帧，请检查摄像头是否正常工作")
        i = 1
        break
cap.release()
cv2.destroyAllWindows()
