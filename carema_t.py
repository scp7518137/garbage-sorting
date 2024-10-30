import cv2

camera_id = 0

# 创建一个VideoCapture对象
cap = cv2.VideoCapture(camera_id)

# 检查是否成功打开了摄像头
if not cap.isOpened():
    print("无法打开摄像头")

while True:
    ret, frame = cap.read()
    if ret:
        height, width, _ = frame.shape
        center_x = width // 2
        center_y = height // 2
        box_size = 50

        start_point = (center_x - box_size, center_y - box_size)
        end_point = (center_x + box_size, center_y + box_size)

        frame = cv2.rectangle(frame, start_point, end_point, color=(0, 255, 0), thickness=1)

        cv2.imshow('Image with Box', frame)

        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    else:
        print("无法获取帧，请检查摄像头是否正常工作")

cap.release()
cv2.destroyAllWindows()
