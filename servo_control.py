import RPi.GPIO as GPIO

class ServoControl:

    def __init__(self, pinNumber):
        self.pinNumber = pinNumber
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pinNumber,GPIO.OUT)
        self.pwm=GPIO.PWM(pinNumber,50)
        self.pwm.start(5)

    def rotateLeft(self, angle):
        self.pwm.ChangeDutyCycle(7.5)

    def rotateRigh(self, angle):
        self.pwm.ChangeDutyCycle(7.5)
