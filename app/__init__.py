from flask import Flask, render_template, Response

from app.servo.pan_tilt_control import PanTillControl
from app.servo.servo_control import ServoControl

app = Flask(__name__)

from app import views
from app import rest_service_servo

# @app.before_first_request
# def initialize():
#     print("Test Init")
