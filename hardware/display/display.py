from RPLCD import *
from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27) #this defines the name of the peripheral (lcd screen) and its address it is used when sending commands

lcd.cursor_pos = (0, 0)
lcd.write_string('Hello World')