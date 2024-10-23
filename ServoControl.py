import serial

LOBOT__FRAME_HEADER              = 0x55
LOBOT_CMD_SERVO_MOVE             = 3
LOBOT_CMD_ACTION_GROUP_RUN       = 6
LOBOT_CMD_ACTION_GROUP_STOP      = 7
LOBOT_CMD_ACTION_GROUP_SPEED     = 11
LOBOT_CMD_GET_BATTERY_VOLTAGE    = 15

serialHandle = serial.Serial("/dev/ttyS0", 9600)  # 初始化串口， 波特率为9600


# 控制单个总线舵机转动
def setBusServoMove(servo_id, servo_pulse, time):
    buf = bytearray(b'\x55\x55')  # 帧头
    buf.append(0x08)  # 数据长度
    buf.append(LOBOT_CMD_SERVO_MOVE)  # 指令
    buf.append(0x01)  # 要控制的舵机个数
    
    time = 0 if time < 0 else time
    time = 30000 if time > 30000 else time
    time_list = list(time.to_bytes(2, 'little'))    # 时间
    buf.append(time_list[0])
    buf.append(time_list[1])    

    servo_id = 254 if (servo_id < 1 or servo_id > 254) else servo_id
    buf.append(servo_id)  # id
    
    servo_pulse = 0 if servo_pulse < 0 else servo_pulse
    servo_pulse = 1000 if servo_pulse > 1000 else servo_pulse
    pulse_list = list(servo_pulse.to_bytes(2, 'little'))    #
    buf.append(pulse_list[0])
    buf.append(pulse_list[1])     

    serialHandle.write(buf)


# 控制单个PWM舵机转动
def setPWMServoMove(servo_id, servo_pulse, time):
    buf = bytearray(b'\x55\x55')  # 帧头
    buf.append(0x08)  # 数据长度
    buf.append(LOBOT_CMD_SERVO_MOVE)  # 指令
    buf.append(0x01)  # 要控制的舵机个数
    
    time = 0 if time < 0 else time
    time = 30000 if time > 30000 else time
    time_list = list(time.to_bytes(2, 'little'))    # 时间
    buf.append(time_list[0])
    buf.append(time_list[1])    

    servo_id = 254 if (servo_id < 1 or servo_id > 254) else servo_id
    buf.append(servo_id)  # 舵机ID
    
    servo_pulse = 500 if servo_pulse < 500 else servo_pulse
    servo_pulse = 2500 if servo_pulse > 2500 else servo_pulse
    pulse_list = list(servo_pulse.to_bytes(2, 'little'))    # 位置
    buf.append(pulse_list[0])
    buf.append(pulse_list[1])     

    serialHandle.write(buf)


# 控制多个总线舵机转动
def setBusServoMoveByArray(servos, servos_count, time):
    buf = bytearray(b'\x55\x55')  # 帧头
    buf.append(servos_count*3+5)  # 数据长度
    buf.append(LOBOT_CMD_SERVO_MOVE)  # 指令
    
    servos_count = 1 if servos_count < 1 else servos_count
    servos_count = 254 if servos_count > 254 else servos_count
    buf.append(servos_count)  # 要控制的舵机个数
    
    time = 0 if time < 0 else time
    time = 30000 if time > 30000 else time
    time_list = list(time.to_bytes(2, 'little'))
    buf.append(time_list[0])    # 时间
    buf.append(time_list[1])
    
    for i in range(servos_count):
        buf.append(servos[i*2])  # 舵机ID
        pos = servos[i*2+1]
        pos = 0 if pos < 0 else pos
        pos = 1000 if pos > 1000 else pos
        pos_list = list(pos.to_bytes(2, 'little'))
        buf.append(pos_list[0])    # 位置
        buf.append(pos_list[1])

    serialHandle.write(buf)


# 控制多个PWM舵机转动
def setPWMServoMoveByArray(servos, servos_count, time):
    buf = bytearray(b'\x55\x55')  # 帧头
    buf.append(servos_count*3+5)  # 数据长度
    buf.append(LOBOT_CMD_SERVO_MOVE)  # 指令
    
    servos_count = 1 if servos_count < 1 else servos_count
    servos_count = 254 if servos_count > 254 else servos_count
    buf.append(servos_count)  # 要控制的舵机个数
    
    time = 0 if time < 0 else time
    time = 30000 if time > 30000 else time
    time_list = list(time.to_bytes(2, 'little'))
    buf.append(time_list[0])    # 时间
    buf.append(time_list[1])
    
    for i in range(servos_count):
        buf.append(servos[i*2])  # 舵机ID

        pos = servos[i*2+1]
        pos = 500 if pos < 500 else pos
        pos = 2500 if pos > 2500 else pos
        pos_list = list(pos.to_bytes(2, 'little'))
        buf.append(pos_list[0])    # 位置
        buf.append(pos_list[1])

    serialHandle.write(buf)


def setGroupRun(group_id, group_count):
    buf = bytearray(b'\x55\x55')  # 帧头
    buf.append(5)  # 数据长度
    buf.append(LOBOT_CMD_ACTION_GROUP_RUN)  # 指令
    buf.append(group_id)   # 动作组id
    count_list = list(group_count.to_bytes(2, 'little'))
    buf.append(count_list[0])    # 次数
    buf.append(count_list[1])
    
    serialHandle.write(buf)


def setGroupStop():
    buf = bytearray(b'\x55\x55')  # 帧头
    buf.append(2)  # 数据长度
    buf.append(LOBOT_CMD_ACTION_GROUP_STOP)  # 指令
    serialHandle.write(buf)


def setGroupSpeed(group_id, group_speed):
    buf = bytearray(b'\x55\x55')  # 帧头
    buf.append(5)  # 数据长度
    buf.append(LOBOT_CMD_ACTION_GROUP_SPEED)  # 指令
    buf.append(group_id)  # 动作组id
    
    speed_list = list(group_speed.to_bytes(2, 'little'))
    buf.append(speed_list[0])    # 速度
    buf.append(speed_list[1])
    serialHandle.write(buf)

def set360PWMServoMoveByArray(servos, servos_count, time):
    buf = bytearray(b'\x55\x55')  # 帧头
    buf.append(servos_count*3+5)  # 数据长度
    buf.append(LOBOT_CMD_SERVO_MOVE)  # 指令

    servos_count = 1 if servos_count < 1 else servos_count
    servos_count = 254 if servos_count > 254 else servos_count
    buf.append(servos_count)  # 要控制的舵机个数

    time = 0 if time < 0 else time
    time = 30000 if time > 30000 else time
    time_list = list(time.to_bytes(2, 'little'))
    buf.append(time_list[0])  # 时间
    buf.append(time_list[1])

    for i in range(servos_count):
        buf.append(servos[i*2])  # 舵机ID

        speed = servos[i*2+1]
        # 限制速度在合理范围内
        speed = 500 if speed < 500 else speed
        speed = 2500 if speed > 2500 else speed
        speed_list = list(speed.to_bytes(2, 'little'))
        buf.append(speed_list[0])  # 速度
        buf.append(speed_list[1])

    serialHandle.write(buf)
