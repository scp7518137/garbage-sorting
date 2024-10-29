import tensorflow as tf
import numpy as np
import cv2
import libraries    # 导入自己写的函数库

model_path1 = 'model/input/best.h5'  # 输入加载模型绝对路径
output_model_path = 'model/'  # 模型输出路径

libraries.conversion_model(model_path1, output_model_path)  # 调用函数

interpreter = tf.lite.Interpreter(model_path=output_model_path)     # 从模型指定路径加载并且创建实例tf.lite.Interpreter使用模型
interpreter.allocate_tensors()  # 为模型所有张量分配空间

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()   # 获取模型的输入和输出细节

cap = cv2.VideoCapture('/dev/video0')  # 选定摄像头
capture_interval = 10   # 拍摄间隔
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 宽度像素
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 高度像素

detected_objects = []  # 用于存储检测到的对象坐标表格

picture_number = 0  # 用于记录图片数量

while True:     # 判断是或否有帧输出，如果没有则终止程序
    ret, frame = cap.read()
    if not ret:
        break

    resized_frame = cv2.resize(frame, (input_details[0]['shape'][1], input_details[0]['shape'][2]))  # 调整图像大小使得图像适合模型
    input_data = np.expand_dims(resized_frame, axis=0)      # 增加维度

    interpreter.set_tensor(input_details[0]['index'], input_data)  # 设置模型张量值，把预处理的图像赋值模型输入层
    interpreter.invoke()  # 调用模型进行推理

    boxes = interpreter.get_tensor(output_details[0]['index'])[0]  # 得到对象边界框
    classes = interpreter.get_tensor(output_details[1]['index'])[0]     # 提取类别
    scores = interpreter.get_tensor(output_details[2]['index'])[0]      # 提取置信度得分
    cv2.imshow('t', frame)

    # 从利用模型图片中提取所有对象的坐标保存在detected_objects列表中
    libraries.add_detected_objects_to_list(boxes, classes, scores, frame.shape[:2], detected_objects)

    print(detected_objects)

    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

detected_objects.clear()  # 清空上一帧的检测结果
cap.release()
cv2.destroyAllWindows()
