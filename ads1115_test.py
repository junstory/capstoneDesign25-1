import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)
if __name__ == "__main__":
    while True:
        chan0 = AnalogIn(ads, ADS.P0)
        chan1 = AnalogIn(ads, ADS.P1)
        print("Channel 0: {}V".format(chan0.voltage))
        print("Channel 1: {}V".format(chan1.voltage))
        time.sleep(1)
