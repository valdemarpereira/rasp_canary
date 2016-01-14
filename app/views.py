from app import app
from app.camera_pi import Camera

@app.route('/')
def index():
    """Video streaming home page."""
    return app.render_template('index.html')

@app.route('/ping')
def index():
	return "Hello, World!"

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return app.Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/servo')
def get(self):
        return {'hello': 'world'}

