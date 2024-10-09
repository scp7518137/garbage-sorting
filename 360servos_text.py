import pigpio
import time

# 初始化pigpio
pi = pigpio.pi()

# 设置GPIO引脚编号
gpio_pin = 27

# 设置PWM频率（通常50Hz对于舵机来说是合适的）
pi.set_PWM_frequency(gpio_pin, 50)

# PWM占空比范围从7.5% (全停) 到 12.5% (全速)
# 根据具体舵机调整这个值，这里只是一个示例
Counterclockwise = 1500
pi.set_servo_pulsewidth(gpio_pin, Counterclockwise)

# 让舵机运行一段时间
time.sleep(20)
# 清理资源
pi.set_PWM_dutycycle(gpio_pin, 0)
pi.set_PWM_frequency(gpio_pin, 0)
pi.stop()
