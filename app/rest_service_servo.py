from app import app, pantill


#from app.servo import ServoControl


@app.route('/servo')
def servo():
    pantill.moveDown(20)
    return "Hello, Servo"