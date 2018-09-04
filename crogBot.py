from firebase import firebase
import time
import RPi.GPIO as GPIO

motorPin = 11
forwardPin = 40
backPin = 13
rightPin = 15
leftPin = 19

#setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(forwardPin, GPIO.OUT)
GPIO.setup(backPin, GPIO.OUT)
GPIO.setup(rightPin, GPIO.OUT)
GPIO.setup(leftPin, GPIO.OUT)
GPIO.setup(motorPin, GPIO.OUT)

#buzzer - disabled currently
#GPIO.setup(40, GPIO.OUT)

#(pin, freq)
servo = GPIO.PWM(motorPin, 50)
servo.start(7.5)

firebase = firebase.FirebaseApplication('https://crogobot.firebaseio.com', None)

def editLight(r):
    if (r == 'up'):
        print ("MOVING FORWARD")
        GPIO.output(forwardPin, GPIO.HIGH)
    elif (r == 'down'):
        print ("MOVING BACKWARD")
        GPIO.output(backPin, GPIO.HIGH)
    elif (r == 'right'):
        print ("TURNING RIGHT")
        GPIO.output(rightPin, GPIO.HIGH)
    elif (r == 'left'):
        print ("TURNING LEFT")
        GPIO.output(leftPin, GPIO.HIGH)
    elif (r == 'horn'):
        print ("SERVO TEST")
        servo.ChangeDutyCycle(2.5)
        time.sleep(1)
        servo.ChangeDutyCycle(12.5)
        #GPIO.output(40, GPIO.LOW)
    else:
        print ("FULL STOP")

#This code will be depricated when I implement the rift stuff!
def setServo(s):
    servo.start(7.5)
    if (s == 'left'):
        print('Servo Left')
        servo.ChangeDutyCycle(12.5)
    elif (s == 'right'):
        print('Servo Right')
        servo.ChangeDutyCycle(2.5)

#TO DO:
# Make this more efficient!!!
while True:
    result = firebase.get('/cont', None)
    editLight(result)

    servoRotation = firebase.get('/servo', None)
    setServo(servoRotation)
    time.sleep(1)

    GPIO.output(forwardPin, GPIO.LOW)
    GPIO.output(backPin, GPIO.LOW)
    GPIO.output(rightPin, GPIO.LOW)
    GPIO.output(leftPin, GPIO.LOW)

    #need to stop the servo to fix the stuttery servo issue
    servo.ChangeDutyCycle(7.5)
    
    time.sleep(0.5)
    # You can play with the values.
    # 7.5 is in most cases the middle position
    # 12.5 is the value for a 180 degree move to the right
    # 2.5 is the value for a -90 degree move to the left

    #Buzzer - disabled
    #GPIO.output(40, GPIO.HIGH)

    




    
