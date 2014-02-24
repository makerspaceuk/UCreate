import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def buzz(pitch, duration):
        period = 1.0 / pitch
        delay = period / 2
        cycles = int(duration * pitch)
        for i in range(cycles):
                GPIO.output(18, True)
                time.sleep(delay)
                GPIO.output(18, False)
                time.sleep(delay)
i=1
while i <4 :
        pitch = 500
        duration = 0.5
        buzz(pitch, duration)
        sleep(2)
        i+=1
GPIO.cleanup()