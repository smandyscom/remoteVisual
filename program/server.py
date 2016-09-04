import BaseHTTPServer
import SimpleHTTPServer
import buttonIncrementor
import pigpio
FILE = 'jquery.html'
PORT = 8060

axis1 = buttonIncrementor.buttonIncrementor()
axis2 = buttonIncrementor.buttonIncrementor()
piController = pigpio.pi()

class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
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
            piController.set_servo_pulsewidth(16, axis1.currentPosition)
            piController.set_servo_pulsewidth(20, axis2.currentPosition)

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
    server.serve_forever()

if __name__ == "__main__":
    # open_browser()
    start_server()
