import StringIO
import time
import BaseHTTPServer
from SocketServer import ThreadingMixIn
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import SimpleHTTPServer
import buttonIncrementor
import pigpio
import io
import picamera

PORT = 8060

axis1 = buttonIncrementor.buttonIncrementor()
axis2 = buttonIncrementor.buttonIncrementor()
piController = pigpio.pi()

cam=None

stream=io.BytesIO()

class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('cam.mjpg'):
            print "handling cam.mjpgl.."
            self.send_response(200)
            self.send_header('Content-type','multipart/x-mixed-replace; boundary=--jpgboundary')
            self.end_headers()
            # index=1
            while True:
            # for foo in cam.capture_continuous(stream,'jpeg'):
                try:
                    value=stream.getvalue()
                    self.wfile.write("--jpgboundary")
                    self.send_header('Content-type','image/jpeg')
                    self.send_header('Content-length',len(value))
                    self.end_headers()
                    self.wfile.write(value)
                    # stream.seek(0)
                    # stream.truncate()
                    # time.sleep(0.05)
                except KeyboardInterrupt:
					break
            return
        if self.path.endswith('index.html'):
            return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
            """The test example handler."""
    def do_POST(self):
        """Handle a post request ."""
        length = int(self.headers.getheader('content-length'))
        data_string = self.rfile.read(length)
        self.wfile.write(data_string) #as response
        # self.wfile.write("server received") #as response
        print 'received:{0}'.format(data_string)
        if data_string == "up":
            axis1.move(True)
        if data_string == "down":
            axis1.move(False)
        if data_string == "left":
            axis2.move(True)
        if data_string == "right":
            axis2.move(False)
        if data_string == "hold":
            piController.set_servo_pulsewidth(16, 0)
            piController.set_servo_pulsewidth(20, 0)
        piController.set_servo_pulsewidth(16, axis1.currentPosition)
        piController.set_servo_pulsewidth(20, axis2.currentPosition)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    # server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
    server = ThreadedHTTPServer(server_address, TestHandler)
    server.serve_forever()

if __name__ == "__main__":
    cam=picamera.PiCamera()
    cam.resolution = (640,480)
    start_server()
