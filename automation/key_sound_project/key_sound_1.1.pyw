import pygame
import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import keyboard
import json
import os

# Initialize Pygame for sound with error handling
try:
    pygame.mixer.init()
    AUDIO_INITIALIZED = True
except Exception as e:
    print(f"Failed to initialize pygame.mixer: {str(e)}")
    AUDIO_INITIALIZED = False

# Sound parameters
SAMPLE_RATE = 44100
VOLUME = 0.3  # Reduced volume for pleasant sound

# Key categories and their default properties
KEY_CATEGORIES = {
    "letters": {
        "keys": list("abcdefghijklmnopqrstuvwxyz"),  # List for JSON
        "pitch_range": [200, 400],  # List for JSON
        "duration": 0.25,
        "waveforms": ["sine", "triangle"],
        "harmonics": True
    },
    "numbers": {
        "keys": list("0123456789"),
        "pitch_range": [400, 600],
        "duration": 0.2,
        "waveforms": ["sine", "square"],
        "harmonics": False
    },
    "symbols": {
        "keys": list("!@#$%^&*()_+-=[]{}|;:,.<>?/~`\"'\\"),
        "pitch_range": [600, 800],
        "duration": 0.15,
        "waveforms": ["square", "sawtooth"],
        "harmonics": False
    },
    "function": {
        "keys": ["esc", "enter", "space", "tab", "backspace", "delete", "insert",
                 "home", "end", "page up", "page down", "up", "down", "left", "right"] +
                [f"f{i}" for i in range(1, 13)],
        "pitch_range": [800, 1000],
        "duration": 0.2,
        "waveforms": ["sine", "triangle"],
        "harmonics": True
    }
}

# Path for config file
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.json")

# Global variables
last_press_time = 0
DEBOUNCE_TIME = 0.1  # seconds
listening = False
root = None
app = None

def apply_adsr_envelope(wave, duration, sample_rate):
    """Apply an ADSR envelope to the waveform."""
    n_samples = len(wave)
    t = np.linspace(0, duration, n_samples, False)
    
    attack = 0.05 * duration
    decay = 0.1 * duration
    sustain = 0.6 * duration
    release = duration - (attack + decay + sustain)
    
    envelope = np.zeros(n_samples)
    attack_samples = int(attack * sample_rate)
    decay_samples = int(decay * sample_rate)
    sustain_samples = int(sustain * sample_rate)
    
    envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
    envelope[attack_samples:attack_samples + decay_samples] = np.linspace(1, 0.7, decay_samples)
    envelope[attack_samples + decay_samples:attack_samples + decay_samples + sustain_samples] = 0.7
    release_samples = n_samples - (attack_samples + decay_samples + sustain_samples)
    envelope[-release_samples:] = np.linspace(0.7, 0, release_samples)
    
    return wave * envelope

def generate_waveform(freq, duration, waveform_type, sample_rate):
    """Generate a waveform of the specified type."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    if waveform_type == "sine":
        wave = np.sin(2 * np.pi * freq * t)
    elif waveform_type == "square":
        wave = np.sign(np.sin(2 * np.pi * freq * t))
    elif waveform_type == "triangle":
        wave = 2 * np.abs(2 * (t * freq - np.floor(t * freq + 0.5))) - 1
    elif waveform_type == "sawtooth":
        wave = 2 * (t * freq - np.floor(t * freq + 0.5))
    else:
        wave = np.sin(2 * np.pi * freq * t)  # Default to sine
    
    return wave

def create_sound(freq, duration, waveform_type, add_harmonic=False):
    """Create a sound with the specified parameters."""
    if not AUDIO_INITIALIZED:
        return None
    
    try:
        wave = generate_waveform(freq, duration, waveform_type, SAMPLE_RATE)
        
        if add_harmonic:
            harmonic_wave = generate_waveform(freq * 2, duration, waveform_type, SAMPLE_RATE)
            wave = 0.7 * wave + 0.3 * harmonic_wave
        
        wave = apply_adsr_envelope(wave, duration, SAMPLE_RATE)
        wave = VOLUME * wave / np.max(np.abs(wave))
        
        stereo_wave = np.array([wave, wave]).T
        stereo_wave = np.ascontiguousarray(stereo_wave)
        
        sound = pygame.sndarray.make_sound((32767 * stereo_wave).astype(np.int16))
        return sound
    except Exception as e:
        print(f"Error creating sound: {str(e)}")
        return None

def get_key_category(key_name):
    """Find the category for the key."""
    for category, info in KEY_CATEGORIES.items():
        if key_name.lower() in info["keys"]:
            return category, info
    return "letters", KEY_CATEGORIES["letters"]

def save_config():
    """Save KEY_CATEGORIES to a JSON file."""
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(KEY_CATEGORIES, f, indent=4)
        return True, "Configuration saved successfully"
    except Exception as e:
        return False, f"Failed to save configuration: {str(e)}"

def load_config():
    """Load KEY_CATEGORIES from a JSON file."""
    global KEY_CATEGORIES
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                loaded_config = json.load(f)
            # Convert lists back to sets and tuples
            for category in loaded_config:
                loaded_config[category]["keys"] = set(loaded_config[category]["keys"])
                loaded_config[category]["pitch_range"] = tuple(loaded_config[category]["pitch_range"])
            KEY_CATEGORIES = loaded_config
            return True, "Configuration loaded successfully"
        else:
            return False, "No configuration file found"
    except Exception as e:
        return False, f"Failed to load configuration: {str(e)}"

class SoundConfigApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Key Sound Configurator")
        
        self.listening = False
        self.log_text = None
        
        self.config_frames = {}
        self.entries = {}
        self.waveform_vars = {}
        self.harmonic_vars = {}
        
        # Load configuration on startup
        success, message = load_config()
        self.create_ui()
        self.log(f"{message}\n")
        if not AUDIO_INITIALIZED:
            self.log("Audio initialization failed. No sound will play.\n")
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def create_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configuration for each category
        for idx, (category, config) in enumerate(KEY_CATEGORIES.items()):
            frame = ttk.LabelFrame(main_frame, text=category.capitalize(), padding="5")
            frame.grid(row=idx, column=0, sticky=(tk.W, tk.E), pady=5)
            self.config_frames[category] = frame
            
            # Frequency range
            ttk.Label(frame, text="Pitch Range (Hz):").grid(row=0, column=0, sticky=tk.W)
            self.entries[(category, "pitch_min")] = ttk.Entry(frame, width=10)
            self.entries[(category, "pitch_min")].insert(0, str(config["pitch_range"][0]))
            self.entries[(category, "pitch_min")].grid(row=0, column=1)
            ttk.Label(frame, text="-").grid(row=0, column=2)
            self.entries[(category, "pitch_max")] = ttk.Entry(frame, width=10)
            self.entries[(category, "pitch_max")].insert(0, str(config["pitch_range"][1]))
            self.entries[(category, "pitch_max")].grid(row=0, column=3)
            
            # Duration
            ttk.Label(frame, text="Duration (s):").grid(row=1, column=0, sticky=tk.W)
            self.entries[(category, "duration")] = ttk.Entry(frame, width=10)
            self.entries[(category, "duration")].insert(0, str(config["duration"]))
            self.entries[(category, "duration")].grid(row=1, column=1)
            
            # Waveforms
            ttk.Label(frame, text="Waveforms:").grid(row=2, column=0, sticky=tk.W)
            self.waveform_vars[category] = {}
            for wave in ["sine", "square", "triangle", "sawtooth"]:
                var = tk.BooleanVar(value=wave in config["waveforms"])
                self.waveform_vars[category][wave] = var
                ttk.Checkbutton(frame, text=wave.capitalize(), variable=var).grid(row=2, column=1+["sine", "square", "triangle", "sawtooth"].index(wave), sticky=tk.W)
            
            # Harmonics
            self.harmonic_vars[category] = tk.BooleanVar(value=config["harmonics"])
            ttk.Checkbutton(frame, text="Add Harmonics", variable=self.harmonic_vars[category]).grid(row=3, column=0, columnspan=2, sticky=tk.W)
            
            # Test Sound button
            ttk.Button(frame, text="Test Sound", command=lambda c=category: self.test_sound(c)).grid(row=3, column=2, columnspan=2, pady=5)
        
        # Control buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=len(KEY_CATEGORIES), column=0, pady=10)
        ttk.Button(control_frame, text="Apply Config", command=self.apply_config).grid(row=0, column=0, padx=5)
        ttk.Button(control_frame, text="Save Config", command=self.save_config_ui).grid(row=0, column=1, padx=5)
        ttk.Button(control_frame, text="Load Config", command=self.load_config_ui).grid(row=0, column=2, padx=5)
        ttk.Button(control_frame, text="Start Listening", command=self.start_listening).grid(row=0, column=3, padx=5)
        ttk.Button(control_frame, text="Stop Listening", command=self.stop_listening).grid(row=0, column=4, padx=5)
        
        # Log area
        self.log_text = tk.Text(main_frame, height=10, width=50)
        self.log_text.grid(row=len(KEY_CATEGORIES)+1, column=0, pady=10)
        self.log_text.insert(tk.END, "Press keys to generate sounds (ESC to stop)\n")
        self.log_text.config(state='disabled')
        
    def test_sound(self, category):
        """Play a test sound for the given category using current settings."""
        try:
            pitch_min = float(self.entries[(category, "pitch_min")].get())
            pitch_max = float(self.entries[(category, "pitch_max")].get())
            duration = float(self.entries[(category, "duration")].get())
            waveforms = [wave for wave, var in self.waveform_vars[category].items() if var.get()]
            add_harmonic = self.harmonic_vars[category].get()
            
            if not waveforms:
                raise ValueError("No waveforms selected")
            if pitch_min >= pitch_max or pitch_min < 20 or pitch_max > 2000:
                raise ValueError("Invalid pitch range")
            if duration <= 0 or duration > 1:
                raise ValueError("Invalid duration")
            
            freq = random.uniform(pitch_min, pitch_max)
            waveform = random.choice(waveforms)
            sound = create_sound(freq, duration, waveform, add_harmonic)
            if sound:
                sound.play()
                self.log(f"Test sound for {category}: {waveform} at {freq:.1f} Hz\n")
            else:
                self.log(f"Failed to create test sound for {category}\n")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def apply_config(self):
        """Apply the configuration from the UI to KEY_CATEGORIES."""
        try:
            for category in KEY_CATEGORIES:
                pitch_min = float(self.entries[(category, "pitch_min")].get())
                pitch_max = float(self.entries[(category, "pitch_max")].get())
                duration = float(self.entries[(category, "duration")].get())
                
                if pitch_min >= pitch_max or pitch_min < 20 or pitch_max > 2000:
                    raise ValueError(f"Invalid pitch range for {category}")
                if duration <= 0 or duration > 1:
                    raise ValueError(f"Invalid duration for {category}")
                
                waveforms = [wave for wave, var in self.waveform_vars[category].items() if var.get()]
                if not waveforms:
                    raise ValueError(f"No waveforms selected for {category}")
                
                KEY_CATEGORIES[category]["pitch_range"] = [pitch_min, pitch_max]
                KEY_CATEGORIES[category]["duration"] = duration
                KEY_CATEGORIES[category]["waveforms"] = waveforms
                KEY_CATEGORIES[category]["harmonics"] = self.harmonic_vars[category].get()
            
            self.log("Configuration applied successfully\n")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def save_config_ui(self):
        """Save configuration from UI."""
        success, message = save_config()
        if success:
            self.log(f"{message}\n")
        else:
            messagebox.showerror("Error", message)
    
    def load_config_ui(self):
        """Load configuration and update UI."""
        success, message = load_config()
        if success:
            # Update UI with loaded values
            for category in KEY_CATEGORIES:
                self.entries[(category, "pitch_min")].delete(0, tk.END)
                self.entries[(category, "pitch_min")].insert(0, str(KEY_CATEGORIES[category]["pitch_range"][0]))
                self.entries[(category, "pitch_max")].delete(0, tk.END)
                self.entries[(category, "pitch_max")].insert(0, str(KEY_CATEGORIES[category]["pitch_range"][1]))
                self.entries[(category, "duration")].delete(0, tk.END)
                self.entries[(category, "duration")].insert(0, str(KEY_CATEGORIES[category]["duration"]))
                for wave in self.waveform_vars[category]:
                    self.waveform_vars[category][wave].set(wave in KEY_CATEGORIES[category]["waveforms"])
                self.harmonic_vars[category].set(KEY_CATEGORIES[category]["harmonics"])
            self.log(f"{message}\n")
        else:
            messagebox.showerror("Error", message)
    
    def start_listening(self):
        """Start capturing key presses globally."""
        if not self.listening:
            self.listening = True
            try:
                keyboard.hook(self.on_key_press)
                self.log("Started listening for key presses (global)\n")
            except Exception as e:
                self.listening = False
                messagebox.showerror("Error", f"Failed to start listening: {str(e)}")
    
    def stop_listening(self):
        """Stop capturing key presses."""
        if self.listening:
            self.listening = False
            try:
                keyboard.unhook_all()
                self.log("Stopped listening\n")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to stop listening: {str(e)}")
    
    def log(self, message):
        """Log a message to the text area."""
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, message)
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')
    
    def on_key_press(self, event):
        """Handle global key press events."""
        global last_press_time
        if not self.listening:
            return
        
        current_time = time.time()
        if current_time - last_press_time < DEBOUNCE_TIME:
            return
        
        key_name = event.name
        if not key_name:  # Skip None or empty key names
            return
        key_name = key_name.lower()
        if key_name == "esc":
            self.stop_listening()
            return
        
        category, info = get_key_category(key_name)
        pitch_min, pitch_max = info["pitch_range"]
        duration = info["duration"]
        waveform = random.choice(info["waveforms"])
        add_harmonic = info["harmonics"]
        
        self.log(f"Key pressed: {key_name} (Category: {category}, Waveform: {waveform})\n")
        
        freq = random.uniform(pitch_min, pitch_max)
        sound = create_sound(freq, duration, waveform, add_harmonic)
        if sound:
            sound.play()
            self.log(f"Playing sound: {waveform} at {freq:.1f} Hz\n")
        else:
            self.log("Failed to play sound\n")
        
        last_press_time = current_time
    
    def on_closing(self):
        """Handle window close event."""
        self.stop_listening()
        self.root.destroy()
        pygame.mixer.quit()

def main():
    """Run the main application."""
    global root, app
    root = tk.Tk()
    app = SoundConfigApp(root)
    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        if app:
            app.stop_listening()
        pygame.mixer.quit()
    finally:
        pygame.mixer.quit()