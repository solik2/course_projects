from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
import socket

class contrl():
    def __init__(self, func_name, agrs):
        pass
    
    def move(data):
        x, y = data
        pass

    def click(data):
        x, y, pressed = data
        pass

    def scroll(data):
        x, y, dx, dy = data
        pass

    def press(key):
        pass

    def release(key):
        pass


def handle_execution():
    state, data = receive()
    execute = getattr(contrl, state)

    
def receive():
    # receive packet and format it
    pass