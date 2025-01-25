import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep              # lets us have a delay
import os 
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(21, GPIO.OUT)           # set GPIO21 as an output   
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)

count = 0
seconds_on = 3600 # Time-out para tiempo máximo encendido


# Our function on what to do when the button is pressed  
def Shutdown(channel):  
    os.system("sudo shutdown -h now")

# Add our function to execute when the button pressed event happens  
GPIO.add_event_detect(20, GPIO.FALLING, callback = Shutdown, bouncetime = 2000) 



try:  
    while True:
        
        GPIO.output(21,0)	#forzada a cero para impedir el reset
        #if GPIO.input(xxx):	#Si instalo un PIR pondré la cuenta a cero
        #    count = 0

        count += 1       

        #print(count) Muestra el valor para depurar

        if count >= seconds_on:
            os.system("sudo shutdown -h now")

        sleep(1)				# wait 1s
            
 
      
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program  
