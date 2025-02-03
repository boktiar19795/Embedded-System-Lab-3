import RPi.GPIO as GPIO
import time

beep_pin = 23
led_pin = 24

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(beep_pin, GPIO.OUT)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(beep_pin, GPIO.HIGH)
    GPIO.output(led_pin, GPIO.LOW)

def loop():
    try:
        while True:
            GPIO.output(beep_pin, GPIO.LOW)
            GPIO.output(led_pin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(beep_pin, GPIO.HIGH)
            GPIO.output(led_pin, GPIO.LOW)
            time.sleep(0.2)
    except KeyboardInterrupt:
        destroy()

def destroy():
    GPIO.output(beep_pin, GPIO.HIGH)
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.cleanup()

if __name__==__main__:
    print('Press Ctrl+C to end the program...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
