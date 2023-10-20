import RPi.GPIO as GPIO
import time

# Define the Buzzer class
class Buzzer:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def play_tone(self, frequency, duration):
        if frequency == 0:
            time.sleep(duration)
            return
        p = GPIO.PWM(self.pin, frequency)
        p.start(50)
        time.sleep(duration)
        p.stop()

# Define the VictoryTune class
class VictoryTune:
    # Define the frequencies for the lower-pitched Mario theme song
    MELODY = [196, 293, 349]

    def __init__(self, buzzer):
        self.buzzer = buzzer

    def play_melody(self):
        for note in self.MELODY:
            if note == 0:
                time.sleep(0.3)  # Pause for 0.3 seconds
            else:
                self.buzzer.play_tone(note, 0.3)  # Play the note for 0.3 seconds


# Usage
if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    buzzer = Buzzer(17)  # Replace with your buzzer's GPIO pin
    mario_tune = VictoryTune(buzzer)
    mario_tune.play_melody()
    GPIO.cleanup()