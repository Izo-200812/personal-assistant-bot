import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Voice Configuration
HOTKEY_COMBINATION = {"ctrl", "shift", "a"}  # Ctrl+Shift+A to activate
VOICE_ENABLED = True
TEXT_ENABLED = True

# Audio Configuration
MICROPHONE_INDEX = None  # Set to specific index if you have multiple mics
SPEECH_TIMEOUT = 5  # seconds to listen for speech
PHRASE_TIME_LIMIT = 30  # max length of audio phrase

# Assistant Configuration
ASSISTANT_NAME = "Assistant"
WAKE_WORD = "hey assistant"
