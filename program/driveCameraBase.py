import threading
import time

class cameraBase:
    def __init__(self, output=None):
        self.output = output

    def serve_forever(self):
        # initialize thread , run method
        def runningCallBack():
            while True:
                try:
                    self.__serve_method__()
                    time.sleep(0.5)
                except KeyboardInterrupt:
                    break
            return

        self.runningThread = threading.Thread(target=runningCallBack)
        self.runningThread.daemon = True
        self.runningThread.start()

    def __serve_method__(self):
        # function should be implemented by derived class
        pass
