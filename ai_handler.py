import openai
from config import OPENAI_API_KEY, MODE, OFFLINE_MODEL

class AIHandler:
    def __init__(self):
        self.mode = MODE
        self.conversation_history = []
        
        if self.mode == "online":
            openai.api_key = OPENAI_API_KEY
        elif self.mode == "offline":
            self.setup_offline_model()
    
    def setup_offline_model(self):
        """Setup offline AI model using transformers"""
        try:
            from transformers import pipeline
            print("🔧 Loading offline model...")
            self.pipeline = pipeline("text-generation", model=OFFLINE_MODEL)
            print("✓ Offline model loaded successfully")
        except ImportError:
            print("❌ Please install transformers: pip install transformers torch")
            raise
        except Exception as e:
            print(f"❌ Error loading offline model: {e}")
            raise
    
    def get_response(self, user_input):
        """Get AI response based on configured mode"""
        try:
            if self.mode == "online":
                return self.get_online_response(user_input)
            elif self.mode == "offline":
                return self.get_offline_response(user_input)
            else:
                return "Invalid mode. Set MODE to 'online' or 'offline' in config.py"
        except Exception as e:
            return f"Error getting response: {str(e)}"
    
    def get_online_response(self, user_input):
        """Get response from OpenAI API"""
        if not OPENAI_API_KEY:
            return "Please set your OpenAI API key in the .env file"
        
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=150
            )
            
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
        
        except openai.error.AuthenticationError:
            return "Invalid OpenAI API key. Please check your .env file"
        except openai.error.RateLimitError:
            return "API rate limit exceeded. Please wait a moment and try again"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_offline_response(self, user_input):
        """Get response using local AI model"""
        try:
            # For a better offline experience, we can use simple pattern matching
            # or a lightweight model
            
            # Simple keyword-based responses for common queries
            responses = {
                "hello": "Hello! How can I help you today?",
                "hi": "Hi there! What do you need?",
                "how are you": "I'm working great! How about you?",
                "what time is it": self.get_time_response(),
                "tell me a joke": self.get_joke(),
                "help": "I can help you with various tasks. Try asking me questions!",
                "bye": "Goodbye! See you next time!",
            }
            
            # Check for keyword matches
            user_input_lower = user_input.lower()
            for keyword, response in responses.items():
                if keyword in user_input_lower:
                    return response
            
            # If no keyword match, use the transformer model
            result = self.pipeline(user_input, max_length=100, num_return_sequences=1)
            return result[0]['generated_text'].strip()
        
        except Exception as e:
            return f"Offline response error: {str(e)}"
    
    def get_time_response(self):
        """Get current time"""
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"
    
    def get_joke(self):
        """Return a random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call a fake noodle? An impasta!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why don't eggs tell jokes? They'd crack each other up!",
        ]
        import random
        return random.choice(jokes)
    
    def reset_conversation(self):
        """Reset conversation history"""
        self.conversation_history = []
    
    def switch_mode(self, new_mode):
        """Switch between offline and online modes"""
        if new_mode not in ["offline", "online"]:
            return "Invalid mode. Choose 'offline' or 'online'"
        
        self.mode = new_mode
        if new_mode == "offline":
            self.setup_offline_model()
        
        return f"Switched to {new_mode} mode"
