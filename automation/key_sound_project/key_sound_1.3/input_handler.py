import time

class InputHandler:
    def __init__(self, config, sound_engine):
        self.config = config
        self.sound_engine = sound_engine
        self.categories = config["key_categories"]
        self.key_debounce = config["key_debounce"]
        self.mouse_debounce = config["mouse_debounce"]
        self.last_key_time = 0
        self.last_mouse_time = 0

    def get_category(self, key_name):
        key_name = key_name.lower()
        for category, data in self.categories.items():
            keys = data["keys"]
            if isinstance(keys, str):
                if key_name in keys:
                    return category, data["pitch_range"]
            elif isinstance(keys, list):
                if key_name in keys:
                    return category, data["pitch_range"]
        return "unknown", (200, 400)

    def handle_key(self, key_name):
        now = time.time()
        if now - self.last_key_time < self.key_debounce:
            return
        category, pitch_range = self.get_category(key_name)
        print(f"[KEY] {key_name} : {category}")
        self.sound_engine.play_random_sound(pitch_range)
        self.last_key_time = now

    def handle_mouse(self, button_name):
        now = time.time()
        if now - self.last_mouse_time < self.mouse_debounce:
            return
        category, pitch_range = self.get_category(button_name)
        print(f"[MOUSE] {button_name} : {category}")
        self.sound_engine.play_random_sound(pitch_range)
        self.last_mouse_time = now 