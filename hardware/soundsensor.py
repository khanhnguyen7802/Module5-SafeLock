import RPi.GPIO as GPIO
import time

# Define the GPIO pin for the sound sensor
SOUND_SENSOR_PIN = 17

# Set up GPIO mode and warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Initialize GPIO pin for the sound sensor
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN)

# Variables to track claps
clap_count = 0
clap_threshold = 2  # Adjust as needed

try:
    while True:
        # Read the digital input from the sound sensor
        sound_detected = GPIO.input(SOUND_SENSOR_PIN)

        if sound_detected:
            clap_count += 1
            print("Sound detected (Clap {})!".format(clap_count))

            # Check if the number of claps reaches the threshold
            if clap_count >= clap_threshold:
                print("Clap detected!")
                # Add your action to be taken when a clap is detected here
                clap_count = 0  # Reset the clap count

        # Add a small delay to avoid rapid clap counting
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO on program exit
    GPIO.cleanup()