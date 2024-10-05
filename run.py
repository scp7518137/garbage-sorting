import tensorflow as tf
import numpy as np
import cv2
import time
import pigpio
import libraries    # 导入自己写的函数库

pi = pigpio.pi()

i = 0

servoPin1 = 1  # x轴舵机
servoPin2 = 2  # y轴舵机
servoPin3 = 3  # 东舵机
servoPin4 = 4  # 南舵机
servoPin5 = 5  # 西舵机
servoPin6 = 6  # 北舵机
servoPin7 = 7  # 中舵机
servoPin8 = 8  # 夹舵机
servoPin9 = 9
servoPin10 = 10
servoPin11 = 11

frequency = 50

zero = 750     # 微秒，对应0度
oh_eighty = 2250    # 微秒，对应180度
ninety = 1500   # 微秒，对应90度

pi.set_servo_pulsewidth(servoPin1, zero)
pi.set_servo_pulsewidth(servoPin2, zero)
pi.set_servo_pulsewidth(servoPin3, zero)
pi.set_servo_pulsewidth(servoPin4, zero)
pi.set_servo_pulsewidth(servoPin5, zero)
pi.set_servo_pulsewidth(servoPin6, zero)
pi.set_servo_pulsewidth(servoPin7, zero)
pi.set_servo_pulsewidth(servoPin8, zero)
pi.set_servo_pulsewidth(servoPin9, zero)
pi.set_servo_pulsewidth(servoPin10, zero)
pi.set_servo_pulsewidth(servoPin11, zero)


# buffer_str = []   # 创建缓存区
model_path1 = '/home/classify/garbage-sorting/model/input/best.h5'  # 输入加载模型绝对路径
output_model_path = '/home/classify/garbage-sorting/model/'  # 模型输出路径

libraries.conversion_model(model_path1, output_model_path)  # 调用函数

interpreter = tf.lite.Interpreter(model_path=output_model_path)     # 从模型指定路径加载并且创建实例tf.lite.Interpreter使用模型
interpreter.allocate_tensors()  # 为模型所有张量分配空间

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()   # 获取模型的输入和输出细节

cap = cv2.VideoCapture('/dev/video14')  # 选定摄像头
# cap.set(cv2.CAP_PROP_FPS, 20)
# actual_fps = cap.get(cv2.CAP_PROP_FPS)
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

    detected_objects.clear()  # 清空上一帧的检测结果

    # 从利用模型图片中提取所有对象的坐标保存在detected_objects列表中
    libraries.add_detected_objects_to_list(boxes, classes, scores, frame.shape[:2], detected_objects)

    if detected_objects:     # 检测detected_objects是否为空
        time.sleep(10)  # 检测到物体延时10秒
        detected_objects.clear()    # 清除列表

        # 再次得到坐标放进列表
        libraries.add_detected_objects_to_list(boxes, classes, scores, frame.shape[:2], detected_objects)
        classified_objects = libraries.classify_class(detected_objects)   # 使用分类函数分开不同种类的垃圾
        # buffer_str.clear()  # 清除缓存列表
        result0 = libraries.order_clamp(classified_objects[0])  # result0包含0位置的所有中心坐标
        # 插入舵机控制程序
        result1 = libraries.order_clamp(classified_objects[1])
        # 插入舵机控制程序
        result2 = libraries.order_clamp(classified_objects[2])
        # 插入舵机控制程序
        result3 = libraries.order_clamp(classified_objects[3])
        # 插入舵机控制程序

        cv2.imshow('show', frame)  # 展示图像
    time.sleep(capture_interval)    # 等待capture_interval秒后拍下一张照片

    if cv2.waitKey(1) & 0xFF == ord('q'):   # 检测到q键之后关闭窗口
        break

cap.release()
cv2.destroyAllWindows()
