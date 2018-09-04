from firebase import firebase
import time
import RPi.GPIO as GPIO

#setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

GPIO.setup(40, GPIO.OUT)

#----
#RUN THIS CODE ON RASP PI
#WILL INCLUDE WIRE DIAGRAM / PICTURE IN REPO
#----

firebase = firebase.FirebaseApplication('https://crogobot.firebaseio.com', None)

def editLight(r):
    if (r == 'up'):
        print ("MOVING FORWARD")
        GPIO.output(11, GPIO.HIGH)
    elif (r == 'down'):
        print ("MOVING BACKWARD")
        GPIO.output(13, GPIO.HIGH)
    elif (r == 'right'):
        print ("TURNING RIGHT")
        GPIO.output(15, GPIO.HIGH)
    elif (r == 'left'):
        print ("TURNING LEFT")
        GPIO.output(19, GPIO.HIGH)
    elif (r == 'horn'):
        print ("HONKING HORN")
        GPIO.output(40, GPIO.LOW)
    else:
        print ("FULL STOP")
        

#TO DO:
# Make this more efficient!!!
while True:
    result = firebase.get('/cont', None)
    #print (result)
    editLight(result)
    time.sleep(1)

    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)

    GPIO.output(40, GPIO.HIGH)