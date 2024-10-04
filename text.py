# cv2.rectangle(frame, (obj['x1'], obj['y1']), (obj['x2'], obj['y2']), (0, 255, 0), 2)  # 绘制边框
# label = f"Class: {int(obj['class'])}, Score: {obj['score']:.2f}"    # 设置标签
# cv2.putText(frame, label, (obj['x1'], obj['y1'] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
# 设置标签坐标值并显示
# picture_number += 1  # 帧数递增
# buffer_str.append(f"Frame: {picture_number}, Object: {index + 1}\n")  # 将数据存放在缓存中
# buffer_str.append(f"Xmin: {obj['x1']}, Ymin: {obj['y1']}, Xmax: {obj['x2']}, Ymax: {obj['y2']}\n")
# buffer_str.append(f"Class: {obj['class']}, Score: {obj['score']:.2f}\n")
# buffer_str.append("\n")
# if len(buffer_str) >= 4:  # 每个对象有4行数据
# with open('object_coordinates.txt', mode='a') as file:
# file.writelines(buffer_str)  # 一次性写入所有数据
# buffer_str.clear()  # 清空缓冲区
# with open('object_coordinates.txt', mode='a') as file:  # 将数据存放在文件
# file.write(f"Frame: {picture_number}, Object: {index + 1}\n")
# file.write(f"Xmin: {obj['x1']}, Ymin: {obj['y1']}, Xmax: {obj['x2']}, Ymax: {obj['y2']}\n")
# file.write(f"Class: {obj['class']}, Score: {obj['score']:.2f}\n")
# file.write("\n")  # 分隔每组数据
# 字典

obj_u = [
    {'class': 0, 'x': 23, 'y': 67},
    {'class': 1, 'x': 56, 'y': 88},
    {'class': 4, 'x': 36, 'y': 88},
    {'class': 2, 'x': 11, 'y': 25},
    {'class': 0, 'x': 36, 'y': 11},
    {'class': 3, 'x': 25, 'y': 34},
    {'class': 2, 'x': 25, 'y': 11},
    {'class': 1, 'x': 25, 'y': 11},
]


def text_az(inp):
    recyclable_waste = []  # 初始化可回收对象
    hazardous_waste = []  # 有害垃圾
    food_waste = []  # 厨余垃圾
    other_waste = []  # 其他垃圾

    # 遍历已检测到的所有对象
    for obj in inp:
        if 0 <= obj['class'] < 1:
            other_waste.append(obj)  # 将符合条件的对象添加到新列表中
        if 1 <= obj['class'] < 2:
            hazardous_waste.append(obj)
        if 2 <= obj['class'] < 3:
            recyclable_waste.append(obj)
        if 3 <= obj['class'] <= 4:
            food_waste.append(obj)

    return other_waste, hazardous_waste, recyclable_waste, food_waste


result = text_az(obj_u)
print(result)
print(result[0])
