#Part of code by CodeBullet: https://youtu.be/wHRubMACen0
#game: http://www.donttap.com/
import sys
import numpy as np
import pyscreenshot as ImageGrab
import cv2
from pyautogui import click, position, onScreen, FAILSAFE, hotkey
import time

FAILSAFE() = True


gameCoords = [463, 107, 890, 535] #x and y coordinats to play within

while True:
#    onScreen(x, y)
    mousePos = position()
    if gameCoords[2] > mousePos.x > gameCoords[0]:
        startTime = time.time()
        screen = np.array(ImageGrab.grab(bbox=gameCoords))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        for y in range(len(screen)):
            for x in range(len(screen[y])):
                if screen[y][x] < 10:
                    click(x, y)
                    pass
        print("Frame took {} seconds, hey ther {}".format((time.time() - startTime), "user"))

exit(esc) #Escape program
