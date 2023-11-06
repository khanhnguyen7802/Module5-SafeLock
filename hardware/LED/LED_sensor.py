import RPi.GPIO as GPIO
import time

LDR_pin = 0
LED_pin = 0

def init_LEDs(LDRpin, LEDpin):

    global LDR_pin, LED_pin

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False) # Ignore warnings

    LDR_pin = LDRpin
    LED_pin = LEDpin

def rc_time (LDR_pin):

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

GPIO.setup(LED_pin, GPIO.OUT, initial=GPIO.LOW)

def check_brightness ():

    """
    This function turns on LED if the brighness is low enough. Call init_LEDs first!
    """
    
    GPIO.setup(LED_pin, GPIO.OUT, initial=GPIO.LOW)
    charge_time = rc_time(LDR_pin)
    print(charge_time)

    if charge_time > 30:
        GPIO.output(LED_pin, GPIO.HIGH)
    else:
        GPIO.output(LED_pin, GPIO.LOW)

#Test code
#try:
#    while True:
#        charge_time = rc_time(LDR_pin)
#        print(charge_time)

#        if charge_time > 30:
#            GPIO.output(LED_pin, GPIO.HIGH)
#        else:
#            GPIO.output(LED_pin, GPIO.LOW)


#except KeyboardInterrupt:
#    pass
#finally:
#    GPIO.cleanup()