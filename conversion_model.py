import tensorflow as tf
import os
import sys


def conversion_model(model_path1, output_model_path):
    if os.path.exists(model_path1):   # 检测该路径下是否存在模型文件
        model = tf.keras.models.load_model(model_path1)   # 模型格式由.h5转化为.tflite
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        converter.optimizations = [tf.lite.Optimize.DEFAULT]    # 混合精度量化模型
        tflite_model = converter.convert()  # 使用转化器进行量化转化，并保存为.tflite

        with open(output_model_path, 'wb') as f:    # 保存到output_model_path路径.tflite文件
            f.write(tflite_model)

    else:
        print("model not found")    # 如果没有该文件，输出并非正常退出
        sys.exit(1)
