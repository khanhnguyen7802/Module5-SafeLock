import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def init_buzzer(pin_number):
    global pin
    pin = pin_number
    
    GPIO.setup(pin, GPIO.OUT)

def play_tone(frequency, duration):
    if frequency == 0:
        time.sleep(duration*0.1)
        return
    tone = GPIO.PWM(pin, frequency)
    tone.start(50)
    time.sleep(duration*0.1)
    tone.stop()
    
def play_melody(melody, durations):
    t = 0
    for tone in melody:
        play_tone(tone, durations[t])
        t += 1