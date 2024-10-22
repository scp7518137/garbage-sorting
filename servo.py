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


spl = [9, 1000, 11, 2000]
spr = [9, 2000, 11, 1000]
spf = [8, 1000, 10, 2000]
spa = [8, 2000, 10, 1000]
stfa = [8, 1500, 10, 1500]
stlr = [9, 1500, 11, 1500]
a = [1, 750, 2, 750, 3, 750, 4, 750]
b = [1, 1100, 2, 950, 3, 1100, 4, 950]

#  下面4放下
ServoControl.setPWMServoMoveByArray(a, 4, 500)
time.sleep(1.5)

#  中心舵机归零
ServoControl.setPWMServoMove(5, 1500, 500)
time.sleep(1)
ServoControl.setPWMServoMove(5, 1300, 500)
time.sleep(1)
ServoControl.setPWMServoMove(5, 1500, 500)
time.sleep(1.5)

#  夹子归零
ServoControl.setPWMServoMove(6, cl, 500)
time.sleep(1)
ServoControl.setPWMServoMove(6, ct, 500)
time.sleep(1)
ServoControl.setPWMServoMove(6, cl, 500)
time.sleep(1.5)

# 旋转归零
ServoControl.setPWMServoMove(7, 750, 1000)
time.sleep(1)
ServoControl.setPWMServoMove(7, 1500, 1000)
time.sleep(1)
ServoControl.setPWMServoMove(7, 750, 1000)
time.sleep(1.5)

# 180抬起
ServoControl.setPWMServoMoveByArray(b, 4, 500)
time.sleep(1.5)

# 360舵机移动
ServoControl.setPWMServoMoveByArray(spl, 2, 500)
time.sleep(3)
ServoControl.setPWMServoMoveByArray(stlr, 2, 500)
time.sleep(1)
ServoControl.setPWMServoMoveByArray(spa, 2, 500)
time.sleep(3)
ServoControl.setPWMServoMoveByArray(stfa, 2, 500)
time.sleep(1.5)

#  夹子松开
ServoControl.setPWMServoMove(6, cl, 500)
time.sleep(1.5)
#  旋转舵机
ServoControl.setPWMServoMove(7, 1000, 500)
time.sleep(1.5)
#  夹子加紧
ServoControl.setPWMServoMove(6, ct, 500)
time.sleep(1.5)

# 360舵机移动
ServoControl.setPWMServoMoveByArray(spl, 2, 500)
time.sleep(3)
ServoControl.setPWMServoMoveByArray(stlr, 2, 500)
time.sleep(1)
ServoControl.setPWMServoMoveByArray(spf, 2, 500)
time.sleep(3)
ServoControl.setPWMServoMoveByArray(stfa, 2, 500)
time.sleep(1.5)

#  放下12舵机
ServoControl.setPWMServoMove(1, al, 500)
time.sleep(1)
ServoControl.setPWMServoMove(2, al, 500)
time.sleep(1.5)

#  夹子松开
ServoControl.setPWMServoMove(6, cl, 500)
time.sleep(1.5)

#  移动归零
ServoControl.setPWMServoMoveByArray(spr, 2, 500)
time.sleep(1)
ServoControl.setPWMServoMoveByArray(stlr, 2, 500)
time.sleep(1.5)

#  旋转归零
ServoControl.setPWMServoMove(7, 750, 500)
time.sleep(1.5)

#  180舵机归零
ServoControl.setPWMServoMoveByArray(b, 4, 500)
time.sleep(1.5)

#  180舵机放下
ServoControl.setPWMServoMoveByArray(a, 4, 500)
time.sleep(1.5)

# 地盘倾斜
ServoControl.setPWMServoMove(5, 1300, 500)
time.sleep(1)
ServoControl.setPWMServoMove(5, 1500, 500)
time.sleep(1)
ServoControl.setPWMServoMove(5, 1300, 500)
time.sleep(1.5)

#  180升高
ServoControl.setPWMServoMoveByArray(b, 4, 500)
time.sleep(0.8)

