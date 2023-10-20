# #!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

SERVO_MIN_PULSE = 500
SERVO_MAX_PULSE = 2500

ServoPin = 11 #GPIO pin

def map(value, inMin, inMax, outMin, outMax):
    return (outMax - outMin) * (value - inMin) / (inMax - inMin) + outMin

def setup():
    global p
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by BCM
    GPIO.setup(ServoPin, GPIO.OUT)   # Set ServoPin's mode is output
    GPIO.output(ServoPin, GPIO.LOW)  # Set ServoPin to low
    p = GPIO.PWM(ServoPin, 50)     # set Frequecy to 50Hz
    p.start(0)                     # Duty Cycle = 0
    
def setAngle(angle):      # make the servo rotate to specific angle (0-180 degrees) 
    angle = max(0, min(180, angle))
    pulse_width = map(angle, 0, 180, SERVO_MIN_PULSE, SERVO_MAX_PULSE)
    pwm = map(pulse_width, 0, 20000, 0, 100)
    p.ChangeDutyCycle(pwm) # map the angle to duty cycle and output it
    
def open_or_close(start, stop, step):
    for i in range(start, stop, step):   #make servo rotate from 0 to 180 deg
        setAngle(i)     # Write to servo
        time.sleep(0.02)
    time.sleep(1)


def loop():
    global password_is_correct, close_safe
    while True:
        if password_is_correct:
            open_or_close(0, 181, 5) #open safe
        if close_safe:
            open_or_close(180,-1,-5)


def destroy():
    p.stop()
    GPIO.cleanup()

if __name__ == '__main__':     #Program starts from here
    setup()
    password_is_correct = True
    close_safe = False
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the program destroy() will be executed.
        destroy()


# =====================================================================================================================

# # Pulse Width Modulation (or PWM) is a technique for controlling power.
# # Duty cycle represents the percentage of time that a signal is high versus low.
# # A PWM signal is characterized by duty cycle which is the percentage of “on time” out of the entire time duration of the pulse.
# # The formula for Selecting the rotation angle based on duty cycle is
# # {DutyCycle = 1/18* (DesiredAngle) + 2}, where DesiredAngle is in degrees.

# import libraries
# import RPi.GPIO as GPIO
# import time 

# # Set GPIO numbering mode 
# GPIO.setmode(GPIO.BOARD)

# # Set pin 11 as an output, and set servo1 as pin 11 as PWM 
# GPIO.setup(11, GPIO.OUT)
# servo1 = GPIO.PWM(11, 50) # 11 is the pin, 50(Hz) is the pulse frequency

# # start PWM running, but with value 0 (pulse off) 
# servo1.start(0) 
# print("Wait 2 secs") 
# time.sleep(2)


# # now move the servo 
# print("Rotate 180 degrees in 10 steps") 

# duty = 2 

# # loop for duty values from 2 to 12 (0-180degrees)
# while duty <= 12:
# 	servo1.ChangeDutyCycle(duty)
# 	time.sleep(0.1) 
# 	duty = duty + 1 
# 	print(duty)
# 	time.sleep(1)
	

# # wait for a couple of seconds 
# time.sleep(2)


# # turn back to 90 degree 
# servo1.ChangeDutyCycle(7) # 7 is between 2 and 12
# time.sleep(2) 


# # turn back to 0 degree 
# print("turning back to 0 degree") 
# servo1.ChangeDutyCycle(2) # back to the initial duty cycle 
# time.sleep(0.5)
# servo1.ChangeDutyCycle(0) 


# # Clean things up at the end 
# servo1.stop() 
# GPIO.cleanup() 
# print("Goodbye")


# ===================

# Loop to allow user to set the servo angle

# try:
# 	while True: 
# 		# Ask user for angle and turn servo to it 
# 		angle = float(input('Enter angle between 0 and 180:'))
# 		servo1.ChangeDutyCycle(2+(angle/18))
# 		time.sleep(0.5)
# 		servo1.ChangeDutyCycle(0)




