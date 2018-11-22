pi@Faceless:~/GPIO $ cat led.py 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
mypin = 8
zzz = 3
GPIO.setwarnings(False)
GPIO.setup(mypin, GPIO.OUT, initial = 0)

try:
        GPIO.output(mypin,GPIO.HIGH)
        #print("ON")
        time.sleep(zzz)
        GPIO.output(mypin,GPIO.LOW)
        #print("OFF")
except KeyboardInterrupt:
        GPIO.cleanup()
        #print("Exiting")
