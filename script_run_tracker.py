import pyautogui
import random
import time
from random import randrange

keyboard_activity = True
mouse_activity    = True
change_tab_screen = True

mouse_activity_loop_time    = 5
keyboard_activity_loop_time = 25


def direction():
    return random.choice(range(100, 600))


def hotkey():
    return random.choice(['command', 'down', 'up', 'fn'])


while True:

    if keyboard_activity:
        for i in range(keyboard_activity_loop_time):
            try:
                pyautogui.press(hotkey())  #keyboard button activity
            except KeyboardInterrupt:
                break
            except:
                pass

    if mouse_activity:
        for i in range(mouse_activity_loop_time):     
            try:
                pyautogui.moveTo(direction(), direction()) #mouse cursor activity
            except KeyboardInterrupt: 
                break
            except:
                pass
    if change_tab_screen:
        # code start for press ctrl+tab for change tab screen
        pyautogui.keyDown('ctrl')
        time.sleep(.2)
        for i in range(randrange(4)):
            pyautogui.press('tab')
            time.sleep(.2)
        pyautogui.keyUp('ctrl')
        # code end 

    time.sleep(random.choice(range(10, 20)))



