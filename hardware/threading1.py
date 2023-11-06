import threading
import time
import sys
import RPi.GPIO as GPIO
import time

name = "dany" #replace this with your username
sys.path.append(f'/home/{name}/Project')
sys.path.append(f'/home/{name}/Project/buzzer')

import led
import soundsensor
import main
import gps
import tcp

t1 = threading.Thread(target=led.ledstart) #thread for leds
t2 = threading.Thread(target=soundsensor.make_sound) #thread for clap function
t3 = threading.Thread(target=main.display_servo_buzzer_keypad) #thread for display, keypad, buzzer and servo
t4 = threading.Thread(target=gps.gps_final_working) #thread for gps
t5 = threading.Thread(target=tcp.send_data) #thread for tcp

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
