import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Mode Configuration
MODE = "online"  # "offline" or "online"
# offline: Uses local AI models (faster, no API costs)
# online: Uses OpenAI API (more accurate, requires API key)

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

# Offline Mode Settings
# Using transformers library for local AI
OFFLINE_MODEL = "distilgpt2"  # Lightweight model for offline use
