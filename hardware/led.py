import RPi.GPIO as GPIO
import time    

def rc_time(LDR_pin):

    GPIO.setup(LDR_pin, GPIO.OUT)
    GPIO.output(LDR_pin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(LDR_pin, GPIO.IN)
    
    start_time = round(time.time()*1000)
    while (GPIO.input(LDR_pin) == GPIO.LOW):
        pass

    end_time = round(time.time()*1000)
        
    time_diff = end_time - start_time

    return time_diff

LDR_pin = 24
LED_pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # Ignore warnings
GPIO.setup(LED_pin, GPIO.OUT)
GPIO.output(LED_pin, GPIO.LOW)
while True:
    charge_time = rc_time(LDR_pin)
    print(charge_time)

    if charge_time > 400:
        GPIO.output(LED_pin, GPIO.HIGH)
    else:
        GPIO.output(LED_pin, GPIO.LOW)
