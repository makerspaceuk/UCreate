import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

Green = GPIO.PWM(18, 100)    
red = GPIO.PWM(22, 100)     

Green.start(0)            
Red.start(100)             

pause_time = 0.02         

try:
    while True:
        for i in range(0,101):      
            Green.ChangeDutyCycle(i)
            Red.ChangeDutyCycle(100 - i)
            sleep(pause_time)
        for i in range(100,-1,-1):      
            Green.ChangeDutyCycle(i)
            Red.ChangeDutyCycle(100 - i)
            sleep(pause_time)
except KeyboardInterrupt:
    Green.stop()           
    Red.stop()              
    GPIO.cleanup()          