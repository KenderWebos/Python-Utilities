import tkinter
import os
from pynput import keyboard

os.system("cls")
print("> Activating HotKeys...")

COMBINATIONS = [
    {keyboard.KeyCode(char = '_'), keyboard.KeyCode(char = '_')}
]

#{keyboard.Key.shift, keyboard.KeyCode(char = 's')},
#{keyboard.Key.shift, keyboard.KeyCode(char = 'S')},

OPENCMD = [
    {keyboard.KeyCode(char = '+')}
]

current = set()

def youtubeSearch():
    query = input("youtube video name: \n")
    query = query.replace(" ", "+")
    os.system("start https://www.youtube.com/results?search_query=" + query)

def on_press(key):
    if any([key in combo for combo in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in combo) for combo in COMBINATIONS):
            youtubeSearch()
    if any([key in combo for combo in OPENCMD]):
        os.system("start")

def on_release(key):
    if any([key in combo for combo in COMBINATIONS]):
        current.remove(key)

print("> HotKeys Activated.")

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

input("finished?")