import openai
from config import OPENAI_API_KEY

class AIHandler:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.conversation_history = []
    
    def get_response(self, user_input):
        """Get AI response from OpenAI API"""
        try:
            if not OPENAI_API_KEY:
                return "Please set your OpenAI API key in the .env file"
            
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Get response from OpenAI
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
        
        except Exception as e:
            return f"Error getting response: {str(e)}"
    
    def reset_conversation(self):
        """Reset conversation history"""
        self.conversation_history = []
