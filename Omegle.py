from pynput.mouse import Button, Controller
import keyboard as kb
import time


mouse = Controller()


def Message():
    mouse.position = 387, 736
    mouse.click(Button.left)
    kb.press_and_release('ctrl+v')
    kb.press_and_release('enter')



def Escape():
    for i in range(4):

        kb.press_and_release('esc')



while True:

    time.sleep(5)

    Message()

    time.sleep(1)

    Escape()


