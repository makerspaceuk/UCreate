import RPi.GPIO as GPIO
 
GPIO.cleanup()
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)
 
while True:
        GPIO.output(15,GPIO.HIGH)
        
