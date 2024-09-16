import tensorflow as tf
import os
import sys
import conversion_model

model_path = ''  # 输入加载模型绝对路径
output_model_path = ''  # 模型输出路径

conversion_model.conversion_model(model_path,output_model_path)#调用函数