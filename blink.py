import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
mypin = 8
counter = 20
zzz = 0.2
GPIO.setwarnings(False)
GPIO.setup(mypin, GPIO.OUT, initial = 0)

try:
        while counter > 0:
                GPIO.output(mypin,GPIO.HIGH)
                time.sleep(zzz)
                GPIO.output(mypin,GPIO.LOW)
                time.sleep(zzz)
                counter -= 1
except KeyboardInterrupt:
        GPIO.cleanup()
        #print("Exiting")
