from pynput import keyboard
from pynput import mouse
import socket

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop keyboard_listener
        return False

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


def listener_handler():
    pass


def keyboard_listener_handler():
    key = keyboard.read_key()
    print(key)
    pass

def mouse_listener_handler():
    pass

# listener_handler()

