import RPi.GPIO as GPIO
import time

#initialize staring values for variables
L1 = 0 
L2 = 0
L3 = 0 
L4 = 0

C1 = 0
C2 = 0
C3 = 0
C4 = 0

GPIO.setwarnings(False) #This turns off the warnings that the RPi.GPIO library generates when you use the pins according to their configurations
GPIO.setmode(GPIO.BCM)# This lets you decide if you want to name the pins according to their physical pin numbers (BOARD) or their SOC channel (BCM)

def init_keypad (row_pin1, row_pin2, row_pin3, row_pin4, col_pin1, col_pin2, col_pin3, col_pin4):

    """
    This presets the pins and pulls down resistors, to initialize the keypad enetr which pins you want to use.
    """

    global L1,L2,L3,L4,C1,C2,C3,C4
    #whch to which pins do the rows go (black wires)
    L1 = row_pin1 
    L2 = row_pin2 
    L3 = row_pin3 
    L4 = row_pin4

    #to which pins do the columns go(white wires)
    C1 = col_pin1
    C2 = col_pin2
    C3 = col_pin3
    C4 = col_pin4

    #GPIO.setwarnings(False) #This turns off the warnings that the RPi.GPIO library generates when you use the pins according to their configurations
    #GPIO.setmode(GPIO.BCM)# This lets you decide if you want to name the pins according to their physical pin numbers (BOARD) or their SOC channel (BCM)

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
        return(characters[0])
    if(GPIO.input(C2) == 1):
        return(characters[1])
    if(GPIO.input(C3) == 1):
        return(characters[2])
    if(GPIO.input(C4) == 1):
        return(characters[3])
    GPIO.output(line, GPIO.LOW)

def check_input():
        x1 = readLine(L1, ["1","2","3","A"])
        if x1 != None:
             time.sleep(0.5)
             return x1
        x2 = readLine(L2, ["4","5","6","B"])
        if x2 != None:
             time.sleep(0.5)
             return x2
        x3 = readLine(L3, ["7","8","9","C"])
        if x3 != None:
             time.sleep(0.5)
             return x3
        x4 = readLine(L4, ["*","0","#","D"])
        if x4 != None:
             time.sleep(0.5)
             return x4
        

#test code

init_keypad(5,6,13,19,12,16,20,21)

try:
    while True:
         keypad_button = None
         keypad_button = check_input()

         if keypad_button != None:
              print(keypad_button)

except KeyboardInterrupt:
    print("\nApplication stopped!")
