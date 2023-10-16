from RPLCD import *
from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27) #this defines the name of the peripheral (lcd screen) and its address it is used when sending commands

def screen_write(pointer_x,pointer_y,text):
    lcd.cursor_pos = (pointer_x, pointer_y)
    lcd.write_string(text)