import time
import pigpio

pi = pigpio.pi()

gpio17 = 17
pi.set_mode(gpio17,pigpio.OUTPUT)

pi.write(gpio17,1)