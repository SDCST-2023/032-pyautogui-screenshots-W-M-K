#!python3
import time 
import pyautogui

start = input("Press enter to start the program: ")
time.sleep(1)
pyautogui.click(213, 388)

while True:
    x = pyautogui.click(213, 388,)
    if pyautogui.locateOnScreen('Golden_cookie.webp', confidence=0.8) is not None:
        pyautogui.click(x=pyautogui.center(pyautogui.locateOnScreen('Golden_cookie.webp', confidence=0.8)).x, y=pyautogui.center(pyautogui.locateOnScreen('Golden_cookie.webp', confidence=0.8)).y )

    if 
    x = pyautogui.click(213, 388,)

    pyautogui.click(1154, 169) 

    pyautogui.click(1283, 840, 3)   
    pyautogui.click(1271, 790, 3)
    pyautogui.click(1277, 727, 3)
    pyautogui.click(1268, 658, 3)

    time.sleep(0.1)
    