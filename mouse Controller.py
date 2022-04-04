from pynput.mouse import Button, Controller
import time
import os

mouse = Controller()
time.sleep(3)

aux = mouse.position
while(1):
    time.sleep(0.05)
    mouse.move(1, 1)
        
