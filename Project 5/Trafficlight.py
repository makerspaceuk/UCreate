import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD);
GPIO.setup(10, GPIO.OUT);
GPIO.setup(12, GPIO.IN);
GPIO.setup(11, GPIO.OUT);
GPIO.setup(13, GPIO.OUT);

i=1
while i < 4:
        if GPIO.input(12):
                GPIO.output(10, False);

        else :
                GPIO.output(10, True);
                sleep(2);
                GPIO.output(11, True);
                sleep(2);
                GPIO.output(10, False);
                GPIO.output(11, False);
                GPIO.output(13, True);
                sleep(2);
                GPIO.output(11, True);
                sleep(2);
                GPIO.output(13, False);
                GPIO.output(11, False);
                GPIO.output(10, True);
                sleep(2);
                i+=1
GPIO.cleanup()