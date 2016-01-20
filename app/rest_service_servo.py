from app import app, PanTillControl, ServoControl

servoh = ServoControl(16)
servov = ServoControl(18)
pantill = PanTillControl(servoh, servov)

print("restServiceServo")

@app.route('/servo')
def servo():
    print("servo_move_debug")
    pantill.moveDown(20)
    return "Hello, Servo"