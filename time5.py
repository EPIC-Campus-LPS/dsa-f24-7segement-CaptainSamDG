# Importing modules and classes

import RPi.GPIO as GPIO
import tm1637
from tm1637 import TM1637
import time
from time import strftime
from time import localtime

GPIO.setmode(GPIO.BCM)
button = 21
light = 5

# Creating 4-digit 7-segment display object
tm = tm1637.TM1637(clk=24, dio=23)  # Using GPIO pins 24 and 23
clear = [0, 0, 0, 0]  # Defining values used to clear the display

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(light, GPIO.OUT)

# Displaying a rolling str
starttime = time.time()

if GPIO.input(button):
    pass
if not GPIO.input(button):
    GPIO.output(light,GPIO.HIGH)
    try:
        while True:
            # Total time elapsed since the timer started
            totaltime = round((time.time() - starttime), 1)

            # Time printed in a time format of Minutes:Seconds of totaltime
            time.sleep(1)
            m = strftime("%M", localtime(totaltime))
            s = strftime("%S", localtime(totaltime))
            m = int(m)
            s = int(s)
            tm.numbers(m, s)

            if not GPIO.input(button) and GPIO.output(light):
                time.sleep(1)
                tm.clear()
                GPIO.output(light, GPIO.LOW)

    except TypeError:
        tm.write(clear)
        GPIO.output(light,GPIO.LOW)
