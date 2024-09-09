from pynput import keyboard
from pynput import mouse
import socket
import time
import threading
from threading import Lock

HOST = '127.0.0.1'
PORT = 6790
controled_device = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

controled_device.connect((HOST, PORT))
# mutex = threading.Lock()

def on_move(x, y):
    # mutex.acquire()
    time.sleep(0.1)
    print('Pointer moved to {0}'.format((x, y)))
    controled_device.send(f"move,{x},{y}\r\n".encode())
    # mutex.release()

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    time.sleep(0.1)
    if pressed:
        controled_device.send(f"mouse_press,{x},{y},{button}\r\n".encode())
    else:
        controled_device.send(f"mouse_release,{x},{y},{button}\r\n".encode())
        

def on_scroll(x, y, dx, dy):
    time.sleep(0.1)
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))
    controled_device.send(f"scroll,{x},{y},{dx},{dy}\r\n".encode())
def on_press(key):
    time.sleep(0.1)
    try:
        print('alphanumeric key {0} pressed'.format(key))
        controled_device.send(f"press,{key.char}\r\n".encode())
    except AttributeError:
        print('special key {0} pressed'.format(key))
        controled_device.send(f"press,{key}\r\n".encode())


def on_release(key):
    time.sleep(0.1)
    print('{0} released'.format(key))
    controled_device.send(f"release,{key}\r\n".encode())
    if key == keyboard.Key.esc:
        # Stop keyboard_listener
        return False

def listener_handler():
    mouse_listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)

    keyboard_listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)

    keyboard_listener.start()
    mouse_listener.start()
    keyboard_listener.join()
    mouse_listener.join()


listener_handler()

