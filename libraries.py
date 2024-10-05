import tensorflow as tf
import os
import sys
import cv2


def conversion_model(model_path1, output_model_path):
    if os.path.exists(model_path1):  # 检测该路径下是否存在模型文件
        model = tf.keras.models.load_model(model_path1)  # 模型格式由.h5转化为.tflite
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        converter.optimizations = [tf.lite.Optimize.DEFAULT]  # 混合精度量化模型
        tflite_model = converter.convert()  # 使用转化器进行量化转化，并保存为.tflite

        with open(output_model_path, 'wb') as f:  # 保存到output_model_path路径.tflite文件
            f.write(tflite_model)

    else:
        print("model not found")  # 如果没有该文件，输出并非正常退出
        sys.exit(1)


# 从利用模型图片中提取所有对象的坐标保存在detected_objects列表中
def add_detected_objects_to_list(boxes, classes, scores, frame_shape, detected_objects):
    for i in range(len(scores)):
        if scores[i] >= 0.5:
            ymin, xmin, ymax, xmax = boxes[i]
            ymin = int(ymin * frame_shape[0])
            xmin = int(xmin * frame_shape[1])
            ymax = int(ymax * frame_shape[0])
            xmax = int(xmax * frame_shape[1])
            # 存储坐标点
            obj_coordinates = {
                'x1': xmin,
                'y1': ymin,
                'x2': xmax,
                'y2': ymax,
                'class': int(classes[i]),
                'score': scores[i]
            }
            detected_objects.append(obj_coordinates)


# 筛选垃圾种类
def classify_class(detected_objects):
    recyclable_waste = []  # 初始化可回收对象
    hazardous_waste = []  # 有害垃圾
    food_waste = []  # 厨余垃圾
    other_waste = []  # 其他垃圾
    # 遍历已检测到的所有对象
    for obj in detected_objects:
        if 0 <= obj['class'] <= 5:
            other_waste.append(obj)  # 将符合条件的对象添加到新列表中
        if 6 <= obj['class'] <= 13:
            hazardous_waste.append(obj)
        if 14 <= obj['class'] <= 36:
            recyclable_waste.append(obj)
        if 37 <= obj['class'] <= 39:
            food_waste.append(obj)
    return recyclable_waste, hazardous_waste, food_waste, other_waste  # 返回筛选后的列表


def order_clamp(list_garbage):
    result = []
    for i in list_garbage:
        x = i['x1']+i['x2']
        y = i['y1']+i['y2']
        result.append([x,y])
    return result
