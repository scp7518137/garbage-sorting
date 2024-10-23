import serial
import time

# 配置串口
ser = serial.Serial(
    port='/dev/ttyS0',  # 根据实际情况修改端口号
    baudrate=9600,  # 波特率，根据控制板的设置调整
    timeout=1  # 读超时，单位为秒
)


def read_data():
    try:
        while True:
            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting)  # 读取所有可用的数据
                print("Received:", data)

                # 解析数据
                if len(data) >= 8 and data[0] == 0x55 and data[1] == 0x55:
                    length = data[2]
                    command = data[3]
                    param1 = data[4]
                    group_number = data[5]
                    run_count = data[6]
                    status_or_error = data[7]

                    print(
                        f"Command: {command}, Group: {group_number}, Count: {run_count}, Status/Error: {status_or_error}")
                else:
                    print("Invalid or incomplete data received.")

            time.sleep(0.1)  # 短暂等待，避免CPU占用过高
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()


if __name__ == "__main__":
    read_data()