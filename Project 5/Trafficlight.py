import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD);
GPIO.setup(10, GPIO.OUT);
GPIO.setup(18, GPIO.IN);
GPIO.setup(12, GPIO.OUT);
GPIO.setup(16, GPIO.OUT);

i=1
try:
	while i < 4:
        	if GPIO.input(18):
                	GPIO.output(10, False);

		else :
                	GPIO.output(10, True);
                	sleep(2);
                	GPIO.output(12, True);
                	sleep(2);
                	GPIO.output(10, False);
                	GPIO.output(12, False);
                	GPIO.output(16, True);
                	sleep(2);
               		GPIO.output(12, True);
                	sleep(2);
                	GPIO.output(16, False);
                	GPIO.output(12, False);
                	GPIO.output(10, True);
                	sleep(2);
                	i+=1
except keyboardInterrupt:
	GPIO.cleanup() 