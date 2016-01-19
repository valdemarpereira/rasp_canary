from flask import Flask, render_template, Response

from app.servo.pan_tilt_control import PanTillControl
from app.servo.servo_control import ServoControl

app = Flask(__name__)

from app import views
from app import rest_service_servo


@app.before_first_request
def initialize(self):
    self.servoh = ServoControl(16)
    self.servov = ServoControl(18)
    self.pantill = PanTillControl(self.servoh, self.servov)
    print("Test Init")
