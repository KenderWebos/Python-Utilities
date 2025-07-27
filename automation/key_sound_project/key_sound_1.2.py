import pygame
import numpy as np
import keyboard
import random
import time
import mouse

# Inicializar Pygame para sonido
pygame.mixer.init()

# Parámetros de sonido
SAMPLE_RATE = 44100
DURATION = 0.2  # segundos

# Categorías de teclas y sus rangos de frecuencia
KEY_CATEGORIES = {
    "letters": {
        "keys": set("abcdefghijklmnopqrstuvwxyz"),
        "pitch_range": (200, 400)
    },
    "numbers": {
        "keys": set("0123456789"),
        "pitch_range": (400, 600)
    },
    "symbols": {
        "keys": set("!@#$%^&*()_+-=[]{}|;:,.<>?/~`\"'\\"),
        "pitch_range": (600, 800)
    },
    "function": {
        "keys": set(["esc", "enter", "space", "tab", "backspace", "delete", "insert",
                     "home", "end", "page up", "page down", "up", "down"] +
                    [f"f{i}" for i in range(1, 13)]),
        "pitch_range": (800, 1000)
    },
    "mouse_left": {
        "keys": {"left"},
        "pitch_range": (1000, 1100)
    },
    "mouse_right": {
        "keys": {"right"},
        "pitch_range": (300, 400)
    },
    "mouse_middle": {
        "keys": {"middle"},
        "pitch_range": (1000, 1100)
    },
    "mouse_wheel": {
        "keys": {"wheel"},
        "pitch_range": (100, 200)
    },
    "volume": {
        "keys": {"volume up", "volume down"},
        "pitch_range": (100, 200)
    }
}

# Variables globales de debounce
last_key_press_time = 0
last_mouse_event_time = 0
KEY_DEBOUNCE = 0.05
MOUSE_DEBOUNCE = 0.01

def create_sound(freq):
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    stereo_wave = np.array([wave, wave]).T
    stereo_wave = np.ascontiguousarray(stereo_wave)
    sound = pygame.sndarray.make_sound((32767 * stereo_wave).astype(np.int16))
    return sound

def get_key_category(key_name):
    for category, info in KEY_CATEGORIES.items():
        if key_name.lower() in info["keys"]:
            return category, info["pitch_range"]
    return "unknown", (200, 400)

def play_key_sound(key_name, is_mouse=False):
    global last_key_press_time, last_mouse_event_time
    current_time = time.time()
    
    if is_mouse:
        if current_time - last_mouse_event_time < MOUSE_DEBOUNCE:
            return
    else:
        if current_time - last_key_press_time < KEY_DEBOUNCE:
            return

    category, (pitch_min, pitch_max) = get_key_category(key_name)
    print(f"Input: {key_name} (Category: {category})")
    freq = random.uniform(pitch_min, pitch_max)
    sound = create_sound(freq)
    sound.play()

    if is_mouse:
        last_mouse_event_time = current_time
    else:
        last_key_press_time = current_time

def on_key_press(event):
    if event.name == "esc":
        print("Exiting...")
        keyboard.unhook_all()
        mouse.unhook_all()
        pygame.mixer.quit()
        raise SystemExit
    play_key_sound(event.name, is_mouse=False)

def on_mouse_event(event):
    if isinstance(event, mouse.ButtonEvent) and event.event_type == "down":
        play_key_sound(event.button, is_mouse=True)
    elif isinstance(event, mouse.WheelEvent):
        play_key_sound("wheel", is_mouse=True)

def main():
    print("Escuchando eventos de teclado y mouse (ESC para salir)")
    print("Categorías: letras (200-400 Hz), números (400-600 Hz), símbolos (600-800 Hz), función (800-1000 Hz), mouse (1000-1200 Hz)")

    keyboard.hook(on_key_press)
    mouse.hook(on_mouse_event)

    try:
        keyboard.wait()
    except SystemExit:
        pass

if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.mixer.quit()
