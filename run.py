import tensorflow as tf
import numpy as np
import cv2
import time
import libraries    # 导入自己写的函数库

buffer_str = []   # 创建缓存区
model_path1 = '/home/classify/garbage-sorting/model/input/best.h5'  # 输入加载模型绝对路径
output_model_path = '/home/classify/garbage-sorting/model/'  # 模型输出路径

libraries.conversion_model(model_path1, output_model_path)  # 调用函数

interpreter = tf.lite.Interpreter(model_path=output_model_path)     # 从模型指定路径加载并且创建实例tf.lite.Interpreter使用模型
interpreter.allocate_tensors()  # 为模型所有张量分配空间

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()   # 获取模型的输入和输出细节

cap = cv2.VideoCapture(0)  # 选定摄像头
# cap.set(cv2.CAP_PROP_FPS, 20)
# actual_fps = cap.get(cv2.CAP_PROP_FPS)
capture_interval = 10   # 拍摄间隔
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 宽度像素
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 高度像素

detected_objects = []  # 用于存储检测到的对象坐标表格

frame_number = 0  # 用于记录帧号

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

    detected_objects.clear()  # 清空上一帧的检测结果

    # 从利用模型图片中提取所有对象的坐标保存在detected_objects列表中
    libraries.add_detected_objects_to_list(boxes, classes, scores, frame.shape[:2], detected_objects)

    if detected_objects:     # 检测detected_objects是否为空
        time.sleep(10)  # 检测到物体延时10秒
        detected_objects.clear()    # 清除列表

        # 再次得到坐标放进列表
        libraries.add_detected_objects_to_list(boxes, classes, scores, frame.shape[:2], detected_objects)

        classified_objects = libraries.classify_class(detected_objects)   # 使用分类函数分开不同种类的垃圾
        buffer_str.clear()  # 清除缓存列表
        for index, obj in enumerate(classified_objects):  # 利用enumerate函数例举出所有对象的值并放在obj当中
            x = (obj['x1'] + obj['x2']) / 2     # 计算中心点x坐标
            y = (obj['y1'] + obj['y2']) / 2     # 计算中心点y坐标

            cv2.rectangle(frame, (obj['x1'], obj['y1']), (obj['x2'], obj['y2']), (0, 255, 0), 2)  # 绘制边框
            label = f"Class: {int(obj['class'])}, Score: {obj['score']:.2f}"    # 设置标签
            cv2.putText(frame, label, (obj['x1'], obj['y1'] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            # 设置标签坐标值并显示
            frame_number += 1  # 帧数递增

            buffer_str.append(f"Frame: {frame_number}, Object: {index + 1}\n")  # 将数据存放在缓存中
            buffer_str.append(f"Xmin: {obj['x1']}, Ymin: {obj['y1']}, Xmax: {obj['x2']}, Ymax: {obj['y2']}\n")
            buffer_str.append(f"Class: {obj['class']}, Score: {obj['score']:.2f}\n")
            buffer_str.append("\n")

            if len(buffer_str) >= 4:  # 每个对象有4行数据
                with open('object_coordinates.txt', mode='a') as file:
                    file.writelines(buffer_str)  # 一次性写入所有数据
                buffer_str.clear()  # 清空缓冲区

            with open('object_coordinates.txt', mode='a') as file:  # 将数据存放在文件
                file.write(f"Frame: {frame_number}, Object: {index + 1}\n")
                file.write(f"Xmin: {obj['x1']}, Ymin: {obj['y1']}, Xmax: {obj['x2']}, Ymax: {obj['y2']}\n")
                file.write(f"Class: {obj['class']}, Score: {obj['score']:.2f}\n")
                file.write("\n")  # 分隔每组数据

                cv2.imshow('show', frame)  # 展示图像
    time.sleep(capture_interval)    # 等待capture_interval秒后拍下一张照片

    if cv2.waitKey(1) & 0xFF == ord('q'):   # 检测到q键之后关闭窗口
        break

cap.release()
cv2.destroyAllWindows()
