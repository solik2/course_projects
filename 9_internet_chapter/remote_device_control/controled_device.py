from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
import socket
import time


HOST = '127.0.0.1'
PORT = 6790

server = socket.socket()
server.bind((HOST, PORT))

server.listen(1)
controlling, address = server.accept()

class contrl():
    def __init__(self, _controller):
        self.controller = _controller
        pass
    
    def move(self,data):
        x, y = data
        x = float(x)
        y = float(y)
        self.controller.position(x, y)

    def mouse_press(self,data):
        x, y, btn = data
        if btn == 'Button.Left':
            self.controller.press(Button.left)
        else:
            self.controller.press(Button.right)



    def mouse_release(self,data):
        x, y, btn = data
        if btn == 'Button.Left':
            self.controller.release(Button.left)
        else:
            self.controller.release(Button.right)


    def scroll(self,data):
        x, y, dx, dy = data
        pass

    def press(self,key):
        pass

    def release(self,key):
        pass


def handle_execution():
    controller = Controller()
    c = contrl(controller)
    while True:
        time.sleep(0.1)
        state, arrgs = receive(controlling)
        print("state: " + str(state))
        print("arrgs: " + str(arrgs))
        execute = getattr(c, state)
        execute(arrgs)

    
def receive(controlling):
    # res = controlling.recv(100).decode("utf-8")
    res = b""

    while True:
        res += controlling.recv(2)
        if res[-2:] == b'\r\n':     # No more data received, quitting
            break
    # print(res)
    data = res.decode()[:-2].split(',')
    return data[0], data[1:]

handle_execution()
