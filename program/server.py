import BaseHTTPServer
import SimpleHTTPServer

FILE = 'jquery.html'
PORT = 8060


class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        """The test example handler."""
        def do_POST(self):
            """Handle a post request ."""
            length = int(self.headers.getheader('content-length'))
            data_string = self.rfile.read(length)
            # self.wfile.write(data_string) #as response
            self.wfile.write("server received") #as response
            print 'received:{0}'.format(data_string)

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
    server.serve_forever()

if __name__ == "__main__":
    # open_browser()
    start_server()
