import RPi.GPIO as GPIO
import time

import sys

name = "dany" #replace this with your username
sys.path.append(f'/home/{name}/Project/buzzer')

import buzzer
import melodies

buzzer.init_buzzer(25)

pin = 17
<<<<<<< HEAD

def init_sound_sensor(number):

    """
    Connect the sensor using 3.3v, GND and pin.
    """
    pin = number
    
    GPIO.setmode (GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

def detect_sound():
    """
    Boolean function. Returns true if clap detected.
    """
    if GPIO.input(pin):
        buzzer.play_melody(melodies.round.MELODY, melodies.round.DURATIONS)
        time.sleep(1)
        return True
        
#test code
init_sound_sensor(17)
while True:
    detect_sound()

=======

def init_sound_sensor(number):

    """
    Connect the sensor using 3.3v, GND and pin.
    """
    pin = number
    
    GPIO.setmode (GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

def detect_sound():
    """
    Boolean function. Returns true if clap detected.
    """
    if GPIO.input(pin):
        buzzer.play_melody(melodies.round.MELODY, melodies.round.DURATIONS)
        time.sleep(1)
        return True
        
#test code
def make_sound():
    init_sound_sensor(17)
    while True:
        detect_sound()

>>>>>>> 47cf3eac0cb0cebd4d7f23e2ca7bba39e97d8e2b