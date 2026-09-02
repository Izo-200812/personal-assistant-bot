#!/usr/bin/env python3
"""
Personal Assistant Bot - Always-active AI assistant
Activation: Press Ctrl+Shift+A or say the wake word
"""

import time
from voice_handler import VoiceHandler
from ai_handler import AIHandler
from hotkey_listener import HotkeyListener
from config import ASSISTANT_NAME, VOICE_ENABLED, TEXT_ENABLED

class PersonalAssistant:
    def __init__(self):
        self.voice_handler = VoiceHandler()
        self.ai_handler = AIHandler()
        self.hotkey_listener = None
        self.is_active = False
        self.setup_hotkeys()
    
    def setup_hotkeys(self):
        """Setup global hotkey listener"""
        self.hotkey_listener = HotkeyListener(self.activate)
        self.hotkey_listener.start()
    
    def activate(self):
        """Activate the assistant"""
        if self.is_active:
            return
        
        self.is_active = True
        print(f"\n✨ {ASSISTANT_NAME} is now active!")
        
        # Listen for command
        if VOICE_ENABLED:
            user_input = self.voice_handler.listen_for_command()
            if not user_input:
                self.is_active = False
                return
        else:
            user_input = input("You: ")
        
        # Get AI response
        print(f"🤔 Thinking...")
        response = self.ai_handler.get_response(user_input)
        
        # Respond with voice or text
        if VOICE_ENABLED:
            self.voice_handler.speak(response)
        else:
            print(f"{ASSISTANT_NAME}: {response}")
        
        self.is_active = False
    
    def run(self):
        """Start the assistant"""
        print(f"""
╔══════════════════════════════════════╗
║   {ASSISTANT_NAME.center(36)}  ║
║  Always-Active AI Assistant          ║
╚══════════════════════════════════════╝

🚀 Bot is running and listening...
Press Ctrl+Shift+A to activate
Type 'exit' to quit

        """)
        
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n\n👋 Shutting down...")
            if self.hotkey_listener:
                self.hotkey_listener.stop()

if __name__ == "__main__":
    assistant = PersonalAssistant()
    assistant.run()
