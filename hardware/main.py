import sys
import RPi.GPIO as GPIO
import time

name = "dany" #replace this with your username
sys.path.append(f'/home/{name}/Project')
sys.path.append(f'/home/{name}/Project/buzzer')


import keypad
import drivers
import buzzer
import melodies

display = drivers.Lcd()

password = "1234"
input = ""
output = "____"
invalid = ["A", "B", "C", "D"]


keypad.init_keypad(5, 13, 19, 26, 12, 16, 20, 21)
buzzer.init_buzzer(17)

def main():
    return 0

def user_interface():
    #open lock
    quit = False
    display.lcd_clear()
    display.lcd_display_string("      unlocked", 2)
    display.lcd_display_string("       #~lock", 4)
    while (not quit):
        character = None
        character = keypad.read()
        if character == "#":
            quit = True
            display.lcd_clear()
            #close lock
        
    


try:
    while True:
        display.lcd_display_string("-------SAFEty-------", 1)
        display.lcd_display_string("   Enter password:", 2)
        display.lcd_display_string("        " + output, 3)
        display.lcd_display_string("*~clear      #~enter", 4)
        
        character = None
        character = keypad.read()
        if character != None:
            if character == "*":
                input = ""
                output = "____"
            elif character == "#":
                display.lcd_clear()
                if input == password:
                    display.lcd_display_string("  Correct password", 1)
                    buzzer.play_melody(melodies.round.MELODY, melodies.round.DURATIONS)
                    user_interface()
                else:
                    display.lcd_display_string(" Incorrect password", 1)
                    buzzer.play_melody(melodies.rickroll.MELODY, melodies.rickroll.DURATIONS)
                    display.lcd_clear()
                output = "____"
                input = ""
            elif len(input) < 4:
                if character not in invalid:
                    input = input + character
                    output = ""
                    i = 0
                    while i < len(input):
                        i += 1
                        output += "*"
                    while len(output) < 4:
                        output += "_"
                else:
                    display.lcd_clear()
                    display.lcd_display_string("       Invalid", 2)
                    display.lcd_display_string("    Only numbers", 4)
                    time.sleep(2)
                    display.lcd_clear()
                    
except KeyboardInterrupt:
    print("\nstopping program")
    display.lcd_clear()