import time
import pigpio
import serial
import ServoControl

a = [1, 800, 2, 800, 3, 800, 4, 800]
b = [1, 1100, 2, 1100, 3, 1100, 4, 1100]
ServoControl.setPWMServoMoveByArray(a, 4, 1000)
time.sleep(2)
ServoControl.setPWMServoMoveByArray(b, 4, 1000)
#ServoControl.setPWMServoMove(1, 800, 1000)
#ServoControl.setPWMServoMove(2, 800, 1000)
#ServoControl.setPWMServoMove(3, 800, 1000)
#ServoControl.setPWMServoMove(4, 800, 1000)
spl = [9,1000,11,2000]
spr = [9,2000,11,1000]
spf = [8,1000,10,2000]
spa = [8,2000,10,1000]
stfa = [8,1500,10,1500]
stlr = [9,1500,11,1500]
#ServoControl.setPWMServoMoveByArray(spa,2,100)
#time.sleep(1)
#ServoControl.setPWMServoMoveByArray(stfa,2,100)
#time.sleep(1)
#ServoControl.setPWMServoMoveByArray(spl,2,100)
