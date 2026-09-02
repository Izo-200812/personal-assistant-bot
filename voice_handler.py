import speech_recognition as sr
import pyttsx3
from config import MICROPHONE_INDEX, SPEECH_TIMEOUT, PHRASE_TIME_LIMIT

class VoiceHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 0.9)  # Volume level
    
    def listen_for_command(self):
        """Listen for voice input and convert to text"""
        try:
            with sr.Microphone(device_index=MICROPHONE_INDEX) as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(
                    source,
                    timeout=SPEECH_TIMEOUT,
                    phrase_time_limit=PHRASE_TIME_LIMIT
                )
            
            text = self.recognizer.recognize_google(audio)
            print(f"✓ You said: {text}")
            return text
        
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"❌ Error with speech recognition: {e}")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"🤖 Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
