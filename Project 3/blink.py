import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)

i=1
try:
	while i < 4 :
		GPIO.output(10, True)
		sleep(1)
		GPIO.output(10, False)
		sleep(1)
		i+=1
except keyboardInterrupt:
	GPIO.cleanup() 