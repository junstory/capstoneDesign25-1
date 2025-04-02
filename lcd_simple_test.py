import RPi_I2C_driver
import time

mylcd = RPi_I2C_driver.lcd()
mylcd.lcd_display_string("Hello!", 1)