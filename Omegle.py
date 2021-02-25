import keyboard as kb
import time




def Message():
    kb.press_and_release('ctrl+v')
    kb.press_and_release('enter')

    print('Message Send')



def Escape():
    for i in range(4):

        kb.press_and_release('esc')



while True:

    time.sleep(5)

    Message()

    time.sleep(1)

    Escape()