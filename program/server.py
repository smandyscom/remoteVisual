import BaseHTTPServer
from SocketServer import ThreadingMixIn
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import SimpleHTTPServer
import buttonIncrementor
# import pigpio
FILE = 'jquery.html'
PORT = 8060

axis1 = buttonIncrementor.buttonIncrementor()
axis2 = buttonIncrementor.buttonIncrementor()
# piController = pigpio.pi()

class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('.mjpg'):
            self.send_response(200)
            self.send_header('Content-type','multipart/x-mixed-replace; boundary=--jpgboundary')
            self.end_headers()
            while True:
				try:
					rc,img = capture.read()
					if not rc:
						continue
					imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
					jpg = Image.fromarray(imgRGB)
					tmpFile = StringIO.StringIO()
					jpg.save(tmpFile,'jpeg')
					self.wfile.write("--jpgboundary")
					self.send_header('Content-type','image/jpeg')
					self.send_header('Content-length',str(tmpFile.len))
					self.end_headers()
					jpg.save(self.wfile,'jpeg')
					time.sleep(0.05)
				except KeyboardInterrupt:
					break
            return
        if self.path.endswith('.html'):
            # return super(TestHandler, self).do_GET(self)
            return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
            """The test example handler."""
    def do_POST(self):
        """Handle a post request ."""
        length = int(self.headers.getheader('content-length'))
        data_string = self.rfile.read(length)
        # self.wfile.write(data_string) #as response
        self.wfile.write("server received") #as response
        print 'received:{0}'.format(data_string)
        if data_string == "up":
            axis1.move(True)
        if data_string == "down":
            axis1.move(False)
        if data_string == "left":
            axis2.move(True)
        if data_string == "right":
            axis2.move(False)
            # piController.set_servo_pulsewidth(16, axis1.currentPosition)
            # piController.set_servo_pulsewidth(20, axis2.currentPosition)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    # server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
    server = ThreadedHTTPServer(server_address, TestHandler)
    server.serve_forever()

if __name__ == "__main__":
    # open_browser()
    start_server()
