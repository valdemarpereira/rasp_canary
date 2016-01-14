from flask import Flask, render_template, Response

from app.servo.pan_tilt_control import PanTillControl
from app.servo.servo_control import ServoControl

app = Flask(__name__)
servoh = ServoControl(16)
servov = ServoControl(18)

pantill = PanTillControl(servoh, servov)

from app import views
from app import rest_service_servo
