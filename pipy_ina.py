#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError

# 18650 배터리의 특성에 맞는 설정
SHUNT_OHMS = 0.1  # 샤프트 저항 (0.1Ω)
#MAX_EXPECTED_AMPS = 2.0  # 예상 최대 전류 (배터리의 최대 전류에 맞게 설정)

def read():
    # INA219 센서 초기화
    ina = INA219(SHUNT_OHMS, 1)
    
    # 16V 범위로 설정 (배터리 전압을 고려한 범위)
    ina.configure(ina.RANGE_16V)
    
    try:
        # 전압, 전류, 전력, 샤프트 전압 출력
        print("Bus Voltage: %.3f V" % ina.voltage())  # 배터리 전압
        print("Bus Current: %.3f mA" % ina.current())  # 전류
        print("Power: %.3f mW" % ina.power())  # 전력
        print("Shunt voltage: %.3f mV" % ina.shunt_voltage())  # 샤프트 전압

    except DeviceRangeError as e:
        # 전류가 설정된 범위를 초과한 경우 예외 처리
        print("DeviceRangeError: %s" % e)

if __name__ == "__main__":
    read()