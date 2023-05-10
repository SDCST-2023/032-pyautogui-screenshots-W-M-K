#!python3
from ctypes import c_int64
import time 
import pyautogui
from PIL import Image
x = 0
y = 0
z = 1
b = 0
c = 0
start = input("Press enter to start the program: ")
print("Just sit back and relax, make sure you don't move your mouse. If you want to exit just move the mouse to the top of the screen quickly.")
pyautogui.PAUSE = 0.01
pyautogui.click(724, 362)
pyautogui.moveTo(1430, 200)
pyautogui.drag(0, 130, duration=1)

pyautogui.click(213, 388)

while x==0:
    while y < 300:
        pyautogui.click(213, 388,)
        y = y + z
    if y == 300:
        c1 = pyautogui.locateOnScreen('Screenshot 2023-05-05 105620.png', confidence=0.5) 
        pyautogui.click(c1) 
        c2 = pyautogui.locateOnScreen('Screenshot 2023-05-05 105635.png', confidence=0.5) 
        pyautogui.click(c2)
        c3 = pyautogui.locateOnScreen('Screenshot 2023-05-05 105712.png', confidence=0.5)
        pyautogui.click(c3)
        c4 = pyautogui.locateOnScreen('Screenshot 2023-05-10 111055.png', confidence=0.5)
        pyautogui.click(c4) 
        c5 = pyautogui.locateOnScreen('Screenshot 2023-05-10 111114.png', confidence=0.5)
        pyautogui.click(c5) 
        c6 = pyautogui.locateOnScreen('Screenshot 2023-05-10 111130.png', confidence=0.5)
        pyautogui.click(c6) 
        c7 = pyautogui.locateOnScreen('Screenshot 2023-05-10 111144.png', confidence=0.5)
        pyautogui.click(c7)
        c8 = pyautogui.locateOnScreen('Screenshot 2023-05-10 111157.png', confidence=0.5)
        pyautogui.click(c8)  
        
        pyautogui.click(1154, 169) 
        pyautogui.click(1283, 840, 3)   
        pyautogui.click(1271, 790, 3)
        pyautogui.click(1277, 727, 2)
        pyautogui.click(1268, 658, 2)
        pyautogui.click(1268, 594, 1)
        pyautogui.click(1268, 532, 1)
        pyautogui.click(1268, 468, 1)
        pyautogui.click(1268, 404, 1)
        pyautogui.click(1268, 348, 1)
        pyautogui.click(1268, 277, 1)
    
    
    y = 0

        
    