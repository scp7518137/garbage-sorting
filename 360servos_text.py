import pigpio
import time

# 初始化pigpio
pi = pigpio.pi()

# 检查是否成功连接到pigpio daemon
if not pi.connected:
    print("Failed to connect to pigpio daemon")
else:
    # 设置GPIO引脚编号
    gpio_pin = 17

    # 设置PWM频率（通常50Hz对于舵机来说是合适的）
    pi.set_PWM_frequency(gpio_pin, 50)

    # 根据具体舵机调整这个值，这里只是一个示例
    Counterclockwise = 2000
    pi.set_servo_pulsewidth(gpio_pin, Counterclockwise)

    # 让舵机运行一段时间
    time.sleep(20)

    # 清理资源
    pi.set_servo_pulsewidth(gpio_pin, 0)
    pi.stop()
