import RPi.GPIO as GPIO, time
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

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
while i <4 :
        pitch = 500
        duration = 0.5
        buzz(pitch, duration)
        sleep(2)
        i+=1
GPIO.cleanup()