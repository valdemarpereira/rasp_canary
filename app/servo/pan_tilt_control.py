class PanTillControl:

    def __init__(self, horzServo, vertServo):
        self.horzServo = horzServo
        self.vertServo = vertServo

    def moveUp(self, angle):
        self.horzServo.rotateRight(angle)

    def moveDown(self, angle):
        self.horzServo.rotateRight(angle)

    def moveLeft(self, angle):
        self.horzServo.rotateLeft(angle)

    def moveRight(self, angle):
        self.horzServo.rotateRight(angle)


