from pynput import keyboard
from pynput import mouse
import socket

HOST = '127.0.0.1'
PORT = 6789 + 1

controled_device = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

controled_device.connect((HOST, PORT))


def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))
    controled_device.send(b'move,{0},{1}', x, y)

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    if pressed:
        controled_device.send(b'mouse_press,{0},{1},{2}', x, y, button)
    else:
        controled_device.send(b'mouse_release,{0},{1},{2}', x, y, button)
        

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))
    controled_device.send(b'scroll,{0},{1},{2},{3}', x, y, dx, dy)

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        controled_device.send(b'press,{0}', key.char)
    except AttributeError:
        print('special key {0} pressed'.format(key))
        controled_device.send(b'press,{0}', key)


def on_release(key):
    print('{0} released'.format(key))
    controled_device.send(b'release, {0}', (key))

    if key == keyboard.Key.esc:
        # Stop keyboard_listener
        return False

def listener_handler():
    while True:
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

