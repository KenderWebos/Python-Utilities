import keyboard
import mouse
from config_loader import load_config
from sound_engine import SoundEngine
from input_handler import InputHandler

def main():
    config = load_config()
    engine = SoundEngine(config)
    handler = InputHandler(config, engine)

    def on_key(event):
        if event.name == "esc":
            print("Exiting...")
            keyboard.unhook_all()
            mouse.unhook_all()
            engine.close()
            raise SystemExit
        handler.handle_key(event.name)

    def on_mouse(event):
        if hasattr(event, 'button') and event.event_type == "down":
            handler.handle_mouse(event.button)
        elif hasattr(event, 'delta'):
            handler.handle_mouse("wheel")

    print("Escuchando eventos de teclado y mouse (ESC para salir)")
    keyboard.hook(on_key)
    mouse.hook(on_mouse)

    try:
        keyboard.wait()
    except SystemExit:
        pass
    finally:
        engine.close()

if __name__ == "__main__":
    main() 