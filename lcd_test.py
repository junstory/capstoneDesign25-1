import RPi_I2C_driver
import time
 
mylcd = RPi_I2C_driver.lcd()
 
i = 0
while True:

    now = time.localtime()
    current_time = time.strftime("%H:%M:%S", now)
    print(current_time)

    mylcd.lcd_display_string("Current Time: " + current_time, 1)
    mylcd.lcd_display_string("Change Check: " +str(i),2)
    mylcd.lcd_display_string("Hello World!",3)
    time.sleep(2)
    mylcd.lcd_clear()
    time.sleep(1)
    i += 1

