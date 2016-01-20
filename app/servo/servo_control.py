import RPi.GPIO as GPIO

class ServoControl:

    minDutyCycle = 3
    maxDutyCycle = 13

    def __init__(self, pinNumber):
        self.pinNumber = pinNumber
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pinNumber,GPIO.OUT)
        self.pwm=GPIO.PWM(pinNumber,50)
        self.pwm.start((self.maxDutyCycle - self.minDutyCycle) / 2)
        print("Servo Init on " + str(self.pinNumber))

    def rotateLeft(self, angle):
        self.pwm.ChangeDutyCycle(self.calculateDutyCycle(angle))

    def rotateRigh(self, angle):
        self.pwm.ChangeDutyCycle(self.calculateDutyCycle(angle))

    def calculateDutyCycle(self, angle):
        return  1/18* (angle) + 3