import RPi.GPIO as GPIO
import time

#whch to which pins do the rows go (black wires)
L1 = 5 #29 (number of the pin)
L2 = 6 #31
L3 = 13 #33
L4 = 19 #35

#to which pins do the columns go(white wires)
C1 = 12 #32
C2 = 16 #36
C3 = 20 #38
C4 = 21 #40

GPIO.setwarnings(False) #This turns off the warnings that the RPi.GPIO library generates when you use the pins according to their configurations
GPIO.setmode(GPIO.BCM)# This lets you decide if you want to name the pins according to their physical pin numbers (BOARD) or their SOC channel (BCM)

GPIO.setup(L1, GPIO.OUT) # Out pin has a volage set to high
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # By setting the pull down resistor we define the logical state of the column to definite 0 when a buttos is pressed the logical state is set to high
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        print(characters[0])
    if(GPIO.input(C2) == 1):
        print(characters[1])
    if(GPIO.input(C3) == 1):
        print(characters[2])
    if(GPIO.input(C4) == 1):
        print(characters[3])
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nApplication stopped!")