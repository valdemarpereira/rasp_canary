from flask import Flask, render_template, Response

from app.servo.pan_tilt_control import PanTillControl
from app.servo.servo_control import ServoControl

app = Flask(__name__)

servoh = None
servov = None
pantill = None

pantill2 = None

from app import views
from app import rest_service_servo

print("blah")

@app.before_first_request
def initialize():
    servoh = ServoControl(16)
    servov = ServoControl(18)
    pantill = PanTillControl(servoh, servov)
    print("Test Init")
