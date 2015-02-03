import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD);
GPIO.setup(10, GPIO.OUT);
GPIO.setup(12, GPIO.IN);

i=1
try:
	while i < 4 :
		if GPIO.input(12):
			GPIO.output(10, False);
		else:
			GPIO.output(10, True);
			sleep(1);
			i+=1
except keyboardInterrupt:
	GPIO.cleanup() 
