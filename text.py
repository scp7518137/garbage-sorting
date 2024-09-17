import tensorflow as tf
import numpy as np
import cv2
import time

import conversion_model

model_path1 = ''  # 输入加载模型绝对路径
output_model_path = ''  # 模型输出路径

conversion_model.conversion_model(model_path1, output_model_path)    # 调用函数

interpreter = tf.lite.Interpreter(model_path=model_path1)
interpreter.allocate_tensors()      # 加载模型

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

cap = cv2.VideoCapture(0)   # 选定摄像头
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)      # 宽度像素
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)     # 高度像素

detected_objects = []  # 用于存储检测到的对象坐标

frame_number = 0  # 用于记录帧号

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized_frame = cv2.resize(frame, (input_details[0]['shape'][1], input_details[0]['shape'][2]))   # 处理图像
    input_data = np.expand_dims(resized_frame, axis=0)

    interpreter.set_tensor(input_details[0]['index'], input_data)  # 图像输入模型
    interpreter.invoke()

    boxes = interpreter.get_tensor(output_details[0]['index'])[0]
    classes = interpreter.get_tensor(output_details[1]['index'])[0]
    scores = interpreter.get_tensor(output_details[2]['index'])[0]

    detected_objects.clear()  # 清空上一帧的检测结果

    for i in range(len(scores)):
        if scores[i] == 1 and 2 and 3:
            ymin, xmin, ymax, xmax = boxes[i]
            ymin = int(ymin * frame.shape[0])
            xmin = int(xmin * frame.shape[1])
            ymax = int(ymax * frame.shape[0])
            xmax = int(xmax * frame.shape[1])


            # 存储坐标点
            obj_coordinates = {
                'xmin': xmin,
                'ymin': ymin,
                'xmax': xmax,
                'ymax': ymax,
                'class': int(classes[i]),
                'score': scores[i]
            }
            detected_objects.append(obj_coordinates)
            if detected_objects:
                
            # 绘制边界框和标签
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
            label = f"Class: {int(classes[i])}, Score: {scores[i]:.2f}"
            cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 显示结果
    cv2.imshow('show', frame)

    # 访问坐标值并进行处理
    frame_number += 1

    # 遍历 `detected_objects` 并访问坐标值
    for index, obj in enumerate(detected_objects):
        x = (obj['xmin'] + obj['xmax'])/2
        y = (obj['ymin'] + obj['ymax'])/2

        # 打印坐标值
        print(f"Object {index + 1}:")
        print(f"X轴距离是 {x}, Y轴距离是{y}")

        # 保存坐标到文件
        with open('object_coordinates.txt', mode='a') as file:
            file.write(f"Frame: {frame_number}, Object: {index + 1}\n")
            file.write(f"Xmin: {xmin}, Ymin: {ymin}, Xmax: {xmax}, Ymax: {ymax}\n")
            file.write(f"Class: {obj['class']}, Score: {obj['score']:.2f}\n")
            file.write("\n")  # 分隔每组数据

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
