import sys
import RPi.GPIO as GPIO
import time

name = "dany" #replace this with your username
sys.path.append(f'/home/{name}/Project')
sys.path.append(f'/home/{name}/Project/buzzer')


import keypad
import drivers
import servo
import buzzer
import melodies
import interfaces
import led

display = drivers.Lcd()

password = {0:"9999",
            1:"1111"
}
input = ""
output = "____"
invalid = ["A", "B", "C", "D"]


keypad.init_keypad(5, 13, 19, 26, 12, 16, 20, 21)
buzzer.init_buzzer(25)
servo.init_servo(11)

def user_interface():
    servo.unlock()
    quit = False
    interfaces.d_print(4)
    while (not quit):
        character = None
        character = keypad.read()
        if character == "A":
            quit = True
            display.lcd_clear()
            servo.lock()

def admin():
    quit = False
    while (not quit):
        interfaces.d_print(5)
        character = None
        character = keypad.read()
        if character == "A":
            state = {"lock":1}
            interfaces.states.update(state)
            servo.unlock()
        elif character == "B":
            settings()
        elif character == "C":
            quit = True

def settings():
    quit = False
    interfaces.d_print(6)
    while (not quit):
        character = None
        character = keypad.read()
        if character == "A":
            i = 1
        elif character == "B":
            i = 2
        elif character == "C":
            quit = True

try:
    servo.lock()
    while True:
        interfaces.d_print(0)
        
        character = None
        character = keypad.read()
        if character != None:
            if character == "*":
                input = ""
                interfaces.output = "____"
            elif character == "#":
                if input == password[0]:
                    interfaces.d_print(2)
                    buzzer.play_melody(melodies.round.MELODY, melodies.round.DURATIONS)
                    user_interface()
                elif input == password[1]:
                    interfaces.d_print(2)
                    buzzer.play_melody(melodies.round.MELODY, melodies.round.DURATIONS)
                    admin()
                else:
                    interfaces.d_print(3)
                    buzzer.play_melody(melodies.rickroll.MELODY, melodies.rickroll.DURATIONS)
                interfaces.output = "____"
                input = ""
            elif len(input) < 4:
                if character not in invalid:
                    input = input + character
                    interfaces.output = ""
                    i = 0
                    while i < len(input):
                        i += 1
                        interfaces.output += "*"
                    while len(interfaces.output) < 4:
                        interfaces.output += "_"
                else:
                    interfaces.d_print(1)
                    
except KeyboardInterrupt:
    print("\nstopping program")
    display.lcd_clear()

