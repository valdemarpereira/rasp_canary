from app import app
#from app.servo import ServoControl

@app.route('/servo')
def servo():
	return "Hello, Servo"