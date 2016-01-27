from app import app
from flask import request
# servoh = ServoControl(16)
# servov = ServoControl(18)
# pantill = PanTillControl(servoh, servov)
from app.servo.servo2 import rotate

print("restServiceServo")

@app.route('/servo')
def servo():
    print("servo_move_debug")
    # pantill.moveDown(20)
    angle = request.args['angle']
    rotate(float(angle))
    return "Hello, Servo"