import os
import RPi_I2C_driver
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#전압 측정 모듈 연결 및 초기화
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

#LCD 모듈 초기화
mylcd = RPi_I2C_driver.lcd()


# ds18b20 온도데이터값을 아래 temp_sensor 경로에 저장하기 위한 명령어
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
# 라즈베리파이가 센서데이터를 받는 경로를 설정(경로는 라즈베리마다 다름))
temp_sensor='/sys/bus/w1/devices/28-0000003860f9/w1_slave'
 
def getVoltage():
    chan = AnalogIn(ads, ADS.P0)
    voltage = chan.voltage
    return voltage

# 파일의 내용을 읽어오는 함수
def temp_raw():
    f = open(temp_sensor,'r')
    lines = f.readlines()
    f.close()
    return lines
 
# 읽어온 파일의 구문을 분석해 온도부분만 반환하는 함수
def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
 
 
    temp_output = lines[1].find('t=')
 
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0/5.0 + 32.0
        return temp_c, temp_f
 
 
while True:
    print(read_temp())
    
    now = time.localtime()
    current_time = time.strftime("%H:%M:%S", now)

    mylcd.lcd_display_string("Current Time: " + current_time, 1)
    mylcd.lcd_display_string("Temp: %.3f C" % read_temp()[0], 2)
    mylcd.lcd_display_string("Temp: %.3f F" % read_temp()[1], 3)
    time.sleep(1)
    mylcd.lcd_clear()

