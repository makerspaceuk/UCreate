import RPi.GPIO as GPIO, time, os
import atexit

DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)

def cleanup():
        GPIO.cleanup()

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.5)

        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading
try:
        while True:
                if RCtime(18) <100 :
                        GPIO.output(2, True)
                        GPIO.output(3, False)
                        GPIO.output(14, False)
                elif RCtime(18) >100 and RCtime(18) <200 :
                        GPIO.output(2, False)
                        GPIO.output(3, True)
                        GPIO.output(14, False)
                elif RCtime(18) >200 :
                        GPIO.output(2, False)
                        GPIO.output(3, False)
                        GPIO.output(14, True)
                print RCtime(18)

except KeyboardInterrupt :
        print ('Exit Program')
atexit.register(cleanup)