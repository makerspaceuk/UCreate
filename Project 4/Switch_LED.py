import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO,BOARD);
GPIO.setup(10, GPIO.OUT);
GPIO.setup(10, GPIO.IN);

i=1
while i < 4 :
	IF GPIO.input(12):
		GPIO.output(10, False);
	Else:
		GPIO.output(10, True);
		sleep(1);
		i+=1
GPIO.cleanup()