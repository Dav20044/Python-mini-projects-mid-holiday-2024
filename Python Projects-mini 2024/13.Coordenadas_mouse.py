#pip install pyautogui
import pyautogui as botMouse
import random
import time 

while True:
    print(botMouse.position())
    x = random.randint(400,900)
    y = random.randint(100,700)

    #botMouse.moveTo(x,y,0.5)
    time.sleep(2)

