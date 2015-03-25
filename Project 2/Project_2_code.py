import RPi.GPIO as GPIO
 
GPIO.cleanup()
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.OUT)

try: 
	while True:
        	GPIO.output(10,GPIO.HIGH)
except keyboardInterrupt:
	GPIO.cleanup() 
