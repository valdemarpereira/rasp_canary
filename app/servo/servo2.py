import RPi.GPIO as GPIO

minDutyCycle = 3
maxDutyCycle = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
pwm=GPIO.PWM(16,50)
pwm.start((maxDutyCycle - minDutyCycle) / 2)
print("Servo Init on 16")

def rotate(angle):
    pwm.ChangeDutyCycle(calculateDutyCycle(angle))

def calculateDutyCycle(angle):
    return  1/18* (angle) + 3