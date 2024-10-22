import time
import serial
import ServoControl


al = 800  # 180电机最低位
a1h = 1100  # 180橙色电机最高位
a2h = 950  # 180黑白电机最高位
bm = 1500  # 最低电机中间位
bi = 1300  # 最低电机倾斜位
cl = 750  # 爪子松开位
ct = 1450  # 爪子紧张位

#  下面五个舵机归零
ServoControl.setBusServoMove(1, al, 1000)
ServoControl.setBusServoMove(2, al, 1000)
ServoControl.setBusServoMove(3, al, 1000)
ServoControl.setBusServoMove(4, al, 1000)
time.sleep(1)

#  夹子舵机归零，旋转舵机归零
ServoControl.setBusServoMove(6, cl, 1000)
ServoControl.setBusServoMove(7, 750, 1000)
time.sleep(1)
ServoControl.setBusServoMove(6, ct, 1000)
ServoControl.setBusServoMove(7, 1500, 1000)
time.sleep(1)
ServoControl.setBusServoMove(6, cl, 1000)
ServoControl.setBusServoMove(7, 750, 1000)
time.sleep(1)

ServoControl.setBusServoMove(5, 1500, 1000)
time.sleep(1)
ServoControl.setBusServoMove(5, 1300, 1000)
time.sleep(1)
ServoControl.setBusServoMove(5, 1500, 1000)
time.sleep(1)

ServoControl.setBusServoMove(1, a1h, 1000)
ServoControl.setBusServoMove(2, a2h, 1000)
ServoControl.setBusServoMove(3, a1h, 1000)
ServoControl.setBusServoMove(4, a2h, 1000)

# 360舵机移动
ServoControl.setBusServoMove(8, 1100, 1000)
ServoControl.setBusServoMove(10, 1100, 1000)
time.sleep(1)
ServoControl.setBusServoMove(9, 1100, 1000)
ServoControl.setBusServoMove(11, 1100, 1000)
time.sleep(1)

#  夹子松开
ServoControl.setBusServoMove(6, cl, 1000)
time.sleep(1)
#  旋转舵机
ServoControl.setBusServoMove(7, 1000, 1000)
time.sleep(1)
#  夹子加紧
ServoControl.setBusServoMove(6, ct, 1000)

# 360舵机移动
ServoControl.setBusServoMove(8, 1100, 1000)
ServoControl.setBusServoMove(10, 1100, 1000)
time.sleep(1)
ServoControl.setBusServoMove(9, 1100, 1000)
ServoControl.setBusServoMove(11, 1100, 1000)
time.sleep(1)

#  放下12
ServoControl.setBusServoMove(1, al, 1000)
ServoControl.setBusServoMove(2, al, 1000)

#  夹子松开
ServoControl.setBusServoMove(6, cl, 1000)
time.sleep(1)

#  移动归零
ServoControl.setBusServoMove(8, 1100, 1000)
ServoControl.setBusServoMove(10, 1100, 1000)
time.sleep(1)
ServoControl.setBusServoMove(9, 1100, 1000)
ServoControl.setBusServoMove(11, 1100, 1000)
time.sleep(1)
#  旋转归零
ServoControl.setBusServoMove(7, 750, 1000)
time.sleep(1)
#  180舵机归零
ServoControl.setBusServoMove(1, 1100, 1000)
ServoControl.setBusServoMove(2, 950, 1000)
time.sleep(2)

#  180舵机放下
ServoControl.setBusServoMove(1, al, 1000)
ServoControl.setBusServoMove(2, al, 1000)
ServoControl.setBusServoMove(3, al, 1000)
ServoControl.setBusServoMove(4, al, 1000)
time.sleep(1)
# 地盘倾斜
ServoControl.setBusServoMove(5, 1300, 1000)
time.sleep(1)
ServoControl.setBusServoMove(5, 1500, 1000)
time.sleep(1)
ServoControl.setBusServoMove(5, 1300, 1000)
time.sleep(1)
#  180升高
ServoControl.setBusServoMove(1, a1h, 1000)
ServoControl.setBusServoMove(2, a2h, 1000)
ServoControl.setBusServoMove(3, a1h, 1000)
ServoControl.setBusServoMove(4, a2h, 1000)
