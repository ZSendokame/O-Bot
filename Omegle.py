import keyboard as kb
import time

https://github.com/ZSendokame/O-Bot
    
def Message():https://github.com/ZSendokame/O-Bot
        
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


