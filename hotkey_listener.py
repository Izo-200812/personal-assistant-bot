from pynput import keyboard
from config import HOTKEY_COMBINATION

class HotkeyListener:
    def __init__(self, callback):
        self.callback = callback
        self.listener = None
        self.pressed_keys = set()
    
    def on_press(self, key):
        """Handle key press"""
        try:
            # Get key name
            if hasattr(key, 'name'):
                self.pressed_keys.add(key.name)
            else:
                self.pressed_keys.add(str(key).replace("'", ""))
            
            # Check if hotkey combination is pressed
            if self.check_hotkey():
                self.callback()
        except AttributeError:
            pass
    
    def on_release(self, key):
        """Handle key release"""
        try:
            if hasattr(key, 'name'):
                self.pressed_keys.discard(key.name)
            else:
                self.pressed_keys.discard(str(key).replace("'", ""))
        except AttributeError:
            pass
    
    def check_hotkey(self):
        """Check if hotkey combination is active"""
        return HOTKEY_COMBINATION.issubset(self.pressed_keys)
    
    def start(self):
        """Start listening for hotkeys"""
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        print(f"🔑 Hotkey listener started. Press {'+'.join(HOTKEY_COMBINATION)} to activate")
    
    def stop(self):
        """Stop listening for hotkeys"""
        if self.listener:
            self.listener.stop()
