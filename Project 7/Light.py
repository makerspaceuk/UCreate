import RPi.GPIO as GPIO, time, os


DEBUG = 1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.5)
        GPIO.setup(RCpin, GPIO.IN)
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading
try:
        while True:
                if RCtime(12) <100 :
                        GPIO.output(14, True)
                        GPIO.output(20, False)
                        GPIO.output(25, False)
                elif RCtime(18) >100 and RCtime(18) <200:
                        GPIO.output(14, False)
                        GPIO.output(20, True)
                        GPIO.output(25, False)
                elif RCtime(18) >200 :
                        GPIO.output(14, False)
                        GPIO.output(20, False)
                        GPIO.output(25, True)
                print RCtime(18)

except KeyboardInterrupt :
        GPIO.cleanup()
