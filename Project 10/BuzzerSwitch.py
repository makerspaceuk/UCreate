import RPi.GPIO as GPIO, time
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(10, GPIO.IN)

def buzz(pitch, duration):
        period = 1.0 / pitch
        delay = period / 2
        cycles = int(duration * pitch)
        for i in range(cycles):
                GPIO.output(12, True)
                time.sleep(delay)
                GPIO.output(12, False)
                time.sleep(delay)
i=1
pitch = 500
duration = 0.5
while i <4 :
        if GPIO.input(10):
                sleep(0.1)
        else:
                buzz(pitch, duration)
                sleep(1)
                i+=1
GPIO.cleanup()
