import time
import pigpio


pi = pigpio.pi()
i = 0
servoPin15 = 15
frequency = 50

zero = 750     # 微秒，对应0度
oh_eighty = 2250    # 微秒，对应180度
ninety = 1500   # 微秒，对应90度

if not pi.connected:
    print("Failed to connect to the Pi.")

else:
    pi.set_mode(servoPin15, pigpio.OUTPUT)
    pi.set_PWM_frequency(servoPin15, frequency)

    # 将伺服设置为0度
    pi.set_servo_pulsewidth(servoPin15, zero)
    time.sleep(1)  # 停留一秒

    # 将伺服设置为90度
    pi.set_servo_pulsewidth(servoPin15, ninety)
    time.sleep(1)  # 停留一秒

    time.sleep(1)
    pi.set_PWM_dutycycle(servoPin15, 0)  # 关闭PWM信号
    pi.stop()  # 断开与pigpio daemon的连接