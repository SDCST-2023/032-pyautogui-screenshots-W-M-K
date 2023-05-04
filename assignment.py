#!python3
import time 
import pyautogui
from PIL import Image
x = 0
y = 0
z = 1
b = 0
c = 0
start = input("Press enter to start the program: ")
print("Just sit back and relax, make sure you don't move your mouse. If you want to exit just move the mouse to the top left of the screen.")
pyautogui.PAUSE = 0.001
pyautogui.moveTo(1430, 200)
pyautogui.drag(0, 130, duration=1)

pyautogui.click(213, 388)

while x==0:
    while y < 5000:
        pyautogui.click(213, 388,)
        y = y + z
        
    if y == 5000:
        pyautogui.click(1154, 169) 

        pyautogui.click(1283, 840, 3)   
        pyautogui.click(1271, 790, 3)
        pyautogui.click(1277, 727, 3)
        pyautogui.click(1268, 658, 3)
        pyautogui.click(1268, 594, 3)
        pyautogui.click(1268, 532, 3)
        pyautogui.click(1268, 468, 3)
        pyautogui.click(1268, 404, 3)
        pyautogui.click(1268, 348, 3)
        pyautogui.click(1268, 277, 3)
    if pyautogui.locateOnScreen('Golden Cookie.png', confidence=0.8) is not None:
        pyautogui.click(x=pyautogui.center(pyautogui.locateOnScreen('Golden Cookie.png', confidence=0.8)).x, y=pyautogui.center(pyautogui.locateOnScreen('Golden Cookie.png', confidence=0.8)).y )
    y = 0

        
    