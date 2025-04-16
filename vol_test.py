# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Sample code and test for adafruit_ina219"""

import time
import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219

# 배터리 전압으로 SOC 초기값 설정
def voltage_to_soc(voltage):
    if voltage >= 4.20:
        return 100
    elif voltage >= 4.10:
        return 90
    elif voltage >= 4.00:
        return 80
    elif voltage >= 3.90:
        return 70
    elif voltage >= 3.80:
        return 60
    elif voltage >= 3.70:
        return 50
    elif voltage >= 3.60:
        return 30
    elif voltage >= 3.50:
        return 20
    elif voltage >= 3.40:
        return 10
    else:
        return 0

i2c_bus = board.I2C()  # uses board.SCL and board.SDA
# i2c_bus = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

ina219 = INA219(i2c_bus)

print("ina219 test")

# display some of the advanced field (just to test)
print("Config register:")
print("  bus_voltage_range:    0x%1X" % ina219.bus_voltage_range)
print("  gain:                 0x%1X" % ina219.gain)
print("  bus_adc_resolution:   0x%1X" % ina219.bus_adc_resolution)
print("  shunt_adc_resolution: 0x%1X" % ina219.shunt_adc_resolution)
print("  mode:                 0x%1X" % ina219.mode)
print("")

# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
# optional : change voltage range to 16V
ina219.bus_voltage_range = BusVoltageRange.RANGE_16V

# measure and display loop
while True:
    bus_voltage = ina219.bus_voltage  # voltage on V- (load side)
    shunt_voltage = ina219.shunt_voltage  # voltage between V+ and V- across the shunt
    current = ina219.current  # current in mA
    power = ina219.power  # power in watts

    internal_resistance = 0.1  # 내부저항 값 (Ω), 실제 측정값으로 정밀화 필요

    '''
    OCV 근사값 계산
    '''
    # 실제 측정값
    bus_voltage = ina219.bus_voltage
    shunt_voltage = ina219.shunt_voltage
    measured_voltage = bus_voltage + shunt_voltage
    current_A = ina219.current / 1000.0

    # OCV 근사값 계산
    ocv_voltage = measured_voltage + (current_A * internal_resistance)

    # SOC 업데이트
    soc = voltage_to_soc(ocv_voltage)
    '''
    END
    '''

    # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
    print("Voltage (VIN+) : {:6.3f}   V".format(bus_voltage + shunt_voltage))
    print("Voltage (VIN-) : {:6.3f}   V".format(bus_voltage))
    print("Shunt Voltage  : {:8.5f} V".format(shunt_voltage))
    print("Shunt Current  : {:7.4f}  A".format(current / 1000))
    print("Power Calc.    : {:8.5f} W".format(bus_voltage * (current / 1000)))
    print("Power Register : {:6.3f}   W".format(power))
    print("ocv_voltage    : {:6.3f}   V".format(ocv_voltage))
    print("SOC           : {:3d} %".format(soc))
    print("")

    # Check internal calculations haven't overflowed (doesn't detect ADC overflows)
    if ina219.overflow:
        print("Internal Math Overflow Detected!")
        print("")

    time.sleep(2)
