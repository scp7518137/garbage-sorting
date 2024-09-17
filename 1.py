import tensorflow as tf
import numpy as np
import cv2

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
while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized_frame = cv2.resize(frame, input_details[0]['shape'][1], input_details[0]['shape'][2])   # 处理图像
    input_data = np.expand_dims(resized_frame, axis=0)

    interpreter.set_tensor(input_details[0]['index'], input_data)  # 图像输入模型
    interpreter.invoke()

    boxes = interpreter.get_tensor(output_details[0]['index'])[0]
    classes = interpreter.get_tensor(output_details[1]['index'])[0]
    scores = interpreter.get_tensor(output_details[2]['index'])[0]

    label = ""
    for i in range(len(scores)):
        if scores[i] >= 0.5:
            ymin, xmin, ymax, xmax = boxes[i]
            cv2.rectangle(frame, (int(xmin * frame.shape[1]), int(ymin * frame.shape[0])),
                          (int(xmax * frame.shape[1]), int(ymax * frame.shape[0])), (0, 255, 0), 2)
            label = "Class: {}, Score: {:.2f}".format(int(classes[i]), scores[i])
            cv2.putText(frame, label, (int(xmin * frame.shape[1]), int(ymin * frame.shape[0]) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('show', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()
