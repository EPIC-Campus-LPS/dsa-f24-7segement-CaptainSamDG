# Importing modules and classes
import tm1637
import time
import numpy as np
from datetime import datetime
from gpiozero import CPUTemperature

# Creating 4-digit 7-segment display object
tm = tm1637.TM1637(clk=4, dio=23)  # Using GPIO pins 18 and 17
clear = [0, 0, 0, 0]  # Defining values used to clear the display

# Displaying a rolling string
tm.write(clear)
time.sleep(1)
s = 'Hello SAM'
tm.scroll(s, delay=200)
time.sleep(2)

