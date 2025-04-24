import pygame
import numpy as np
import keyboard
import random
import time

# Initialize Pygame for sound
pygame.mixer.init()

# Sound parameters
SAMPLE_RATE = 44100
DURATION = 0.2  # seconds

# Key categories and their pitch ranges (in Hz)
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
                     "home", "end", "page up", "page down", "up", "down", "left", "right"] +
                    [f"f{i}" for i in range(1, 13)]),
        "pitch_range": (800, 1000)
    }
}

# Global variable to track last key press time
last_press_time = 0
DEBOUNCE_TIME = 0.1  # seconds

def create_sound(freq):
    # Create a sine wave
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    # Convert to stereo (2D array)
    stereo_wave = np.array([wave, wave]).T
    # Ensure C-contiguous array
    stereo_wave = np.ascontiguousarray(stereo_wave)
    # Create sound
    sound = pygame.sndarray.make_sound((32767 * stereo_wave).astype(np.int16))
    return sound

def get_key_category(key_name):
    # Find the category for the key
    for category, info in KEY_CATEGORIES.items():
        if key_name.lower() in info["keys"]:
            return category, info["pitch_range"]
    return "unknown", (200, 400)  # Default to letters' pitch range for unknown keys

def on_key_press(event):
    global last_press_time
    current_time = time.time()
    
    # Ignore if too soon after last press (debouncing)
    if current_time - last_press_time < DEBOUNCE_TIME:
        return
    
    # Check for ESC to exit
    if event.name == "esc":
        print("Exiting...")
        keyboard.unhook_all()
        pygame.mixer.quit()
        raise SystemExit
    
    # Get key category and pitch range
    category, (pitch_min, pitch_max) = get_key_category(event.name)
    
    # Print key name and category
    print(f"Key pressed: {event.name} (Category: {category})")
    
    # Play sound with random frequency in the category's pitch range
    freq = random.uniform(pitch_min, pitch_max)
    sound = create_sound(freq)
    sound.play()
    
    # Update last press time
    last_press_time = current_time

def main():
    print("Listening for key presses (press ESC to quit)")
    print("Categories: letters (200-400 Hz), numbers (400-600 Hz), symbols (600-800 Hz), function (800-1000 Hz)")
    # Set up key press hook
    keyboard.hook(on_key_press)
    # Keep the program running
    try:
        keyboard.wait()
    except SystemExit:
        pass

if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.mixer.quit()