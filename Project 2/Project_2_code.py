import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(10,GPIO.OUT)

try: 
	while True:
        	GPIO.output(10,GPIO.HIGH)
except keyboardInterrupt:
	GPIO.cleanup() 
