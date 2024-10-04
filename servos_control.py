import pigpio
import time

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

pi.set_servo_pulsewidth(servoPin1,zero)
pi.set_servo_pulsewidth(servoPin2,zero)
pi.set_servo_pulsewidth(servoPin3,zero)
pi.set_servo_pulsewidth(servoPin4,zero)
pi.set_servo_pulsewidth(servoPin5,zero)
pi.set_servo_pulsewidth(servoPin6,zero)
pi.set_servo_pulsewidth(servoPin7,zero)
pi.set_servo_pulsewidth(servoPin8,zero)
pi.set_servo_pulsewidth(servoPin9,zero)
pi.set_servo_pulsewidth(servoPin10,zero)
pi.set_servo_pulsewidth(servoPin11,zero)

time.sleep(2)


