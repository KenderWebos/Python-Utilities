from pyautogui import *
import pyautogui
import time
import keyboard
import random
import os

def clickOn(interX, interY):
    pyautogui.mouseDown(x = interX, y= interY)
    pyautogui.mouseUp(x = interX, y= interY)


clickOn(900, 550)
