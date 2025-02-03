import RPi.GPIO as GPIO
import time

BeepPin = 11    # pin11

def setup():
    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    GPIO.setup(BeepPin, GPIO.OUT)   # Set BeepPin's mode as output
    GPIO.output(BeepPin, GPIO.HIGH) # Set BeepPin high(+3.3V) to turn off beep

def loop():
    while True:
        GPIO.output(BeepPin, GPIO.LOW)  # Switch on the buzzer
        time.sleep(0.1)                 # 0.1s delay
        GPIO.output(BeepPin, GPIO.HIGH) # Switch off the buzzer
        time.sleep(0.1)

def destroy():
    GPIO.output(BeepPin, GPIO.HIGH)    # Turn off the buzzer
    GPIO.cleanup()                     # Release resources

print('Press Ctrl+C to end the program...')

setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
