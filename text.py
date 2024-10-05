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
#table = [
    #["Name", "Age", "Position"],
    #["Alice", 30, "Developer"],
    #["Bob", 25, "Designer"],
    #["Charlie", 35, "Manager"]
#]

#for row in table:
    #for column in row:
        #print(column, end="\t")  # 使用制表符分隔列数据
    #print()  # 每行结束后换行

# tup = (1, 2, 3, 4, 5)

# for item in tup:
    # print(item)

dictionary = {
    "class": "fruit",
    "x1": 63,
    "y1": 74,
    "x2": 26,
    "y2": 51,
}
a = dictionary
x1 = a["x1"]
y1 = a["y1"]
x2 = a["x2"]
y2 = a["y2"]
x = (x1 + x2)/2
y = (y1 + y2)/2
print(x, y)





# 只遍历键
#for a in dictionary:
   #print(a)
# 或者使用keys()方法
#for a in dictionary.keys():
    #print(a)
# 遍历键值对
# a, b in dictionary.items():
   # print(f"{a}: {b}")
# 遍历值
#for asd in dictionary.values():
    #print(asd)