#Part of code by CodeBullet: https://youtu.be/wHRubMACen0
#game: http://www.donttap.com/
import sys
import numpy as np
import pyscreenshot as ImageGrab
import cv2
#from pyautogui import click, position, onScreen, FAILSAFE, hotkey, PAUSE
import pyautogui
import time

pyautogui.FAILSAFE = True

input("Start by pressing enter")
time.sleep(3)

gameCoords = [463, 205, 890, 635] #(left_x, top_y, right_x, bottom_y)

while True:
#    pyautogui.onScreen(x, y)
    mousePosx, mousePosy = pyautogui.position()
    print(mousePosx, mousePosy)
    if gameCoords[2] > mousePosx > gameCoords[0]: #mousePos[0] = x coordinate
        print("line 23:", "1:", gameCoords[0],"2:", gameCoords[2])
        startTime = time.time()
        screen = np.array(ImageGrab.grab(bbox=gameCoords)) #take screenshot within gameCoords
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY) #cvtColor(input, output, color)
        for y in range(len(screen)):
            for x in range(len(screen[y])):
                if screen[y][x] < 10 and gameCoords[2] > screen[x] > gameCoords[0]:
                    print("line: 30:", mousePosx, mousePosy)
                    pyautogui.click(x, y)
                    time.sleep(2.5) #pause pyautogui for 2.5 sec
                    pass
        print("Frame took {} seconds, hey ther {}".format((time.time() - startTime), "user"))
        if pyautogui.hotkey(esc):
            exit()

exit(esc) #Escape program
