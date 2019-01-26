#Part of code by CodeBullet: https://youtu.be/wHRubMACen0
import numpy as np
import pyscreenshot as ImageGrab
import cv2
from directKeys import click, queryMousePosition
import time

gameCoords = [corner1, corner2, corner3, corner4] #coordinats to play within

screen = np.array(ImageGrab.grab(bbox=gameCoords))
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

while True:
    mousePos = queryMousePosition()
    if gameCoords[2] > mousePos.x > gameCoords[0]:
        startTime = time.time()
        for y in range(len(screen)):
            for x in range(len(screen[y])):
                if screen[y][x] < 10:
                    #click(x, y)
                    pass
    print("Frame tooke {} seconds".format((time.time() - startTime, i)))

exit(esc) #Escape program
