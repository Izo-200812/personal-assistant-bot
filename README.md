# 🤖 Personal Assistant Bot

An always-active AI assistant application that responds to your commands via voice or text. Similar to Siri, it runs in the background and can be activated with a hotkey. **Supports both OFFLINE and ONLINE modes!**

## ✨ Features

- 🎤 **Voice Recognition** - Speak commands naturally
- 🔊 **Text-to-Speech** - Hear responses from the bot
- ⌨️ **Hotkey Activation** - Press `Ctrl+Shift+A` to activate
- 🧠 **Dual AI Modes:**
  - **Online Mode** - Uses OpenAI's GPT-3.5 (more accurate)
  - **Offline Mode** - Uses local AI models (no API costs, instant response)
- 💬 **Conversation Memory** - Maintains context across interactions
- 🔄 **Mode Switching** - Switch between online and offline anytime
- 🔧 **Configurable** - Easy customization via config.py

## 📋 Requirements

- Python 3.7+
- Microphone for voice input
- Speaker for voice output
- Windows, macOS, or Linux
- OpenAI API key (only needed for online mode)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Izo-200812/personal-assistant-bot.git
cd personal-assistant-bot
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure (Optional - for Online Mode)
If you want to use **Online Mode** with OpenAI API:

1. Get your API key from [OpenAI](https://platform.openai.com/api-keys)
2. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Add your API key to `.env`:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

### 5. Run the Bot
```bash
python main.py
```

## 🎮 Usage

### Starting the Bot
```bash
python main.py
```

### Activating the Bot
- Press `Ctrl+Shift+A` (or configured hotkey)
- The bot will say "Assistant is now active! [MODE]"

### Giving Commands
- Speak your command or type it
- Wait for the response

### Switching Modes
- Say or type: **"switch to online"** - Use OpenAI API (more powerful)
- Say or type: **"switch to offline"** - Use local AI (no API costs)

### Example Commands
```
"What's the weather?"
"Tell me a joke"
"What is Python?"
"How do I write a function?"
"What time is it?"
"Hello"
"switch to offline"
"switch to online"
```

## 🔌 Online vs Offline Mode

### 🌐 Online Mode
```python
MODE = "online"
```
- **Pros:** Better responses, understands complex questions
- **Cons:** Requires API key, costs money, needs internet
- **Best for:** Complex queries, conversations

### 🏠 Offline Mode
```python
MODE = "offline"
```
- **Pros:** Free, instant, no internet needed, privacy
- **Cons:** Simpler responses, limited knowledge
- **Best for:** Quick answers, no internet, privacy-conscious use

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Switch between modes
MODE = "offline"  # "offline" or "online"

# Change hotkey combination
HOTKEY_COMBINATION = {"ctrl", "shift", "a"}

# Enable/disable voice
VOICE_ENABLED = True
TEXT_ENABLED = True

# Microphone settings
MICROPHONE_INDEX = None
SPEECH_TIMEOUT = 5
PHRASE_TIME_LIMIT = 30

# Bot name
ASSISTANT_NAME = "Assistant"

# Offline model
OFFLINE_MODEL = "distilgpt2"
```

## 📁 Project Structure

```
personal-assistant-bot/
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── voice_handler.py       # Speech recognition & TTS
├── ai_handler.py          # AI logic (online & offline)
├── hotkey_listener.py     # Global hotkey listener
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── .env                   # Your actual API keys (don't commit)
└── README.md              # This file
```

## 🔧 Troubleshooting

### Microphone not detected
- Check if your microphone is properly connected
- In `config.py`, set `MICROPHONE_INDEX` to a specific device:
  ```python
  # Run this to list available microphones
  import speech_recognition as sr
  mic_list = sr.Microphone.list_microphone_indexes()
  for i, mic in enumerate(mic_list):
      print(f"{i}: {mic}")
  ```

### Offline mode not working
- Ensure PyTorch is installed correctly
- For GPU support, install CUDA: https://pytorch.org/get-started/locally/
- Or use CPU version (slower but works)

### Voice output not working
- Ensure speakers are enabled
- Check volume levels
- Install audio drivers for your OS

### API Key errors (Online Mode)
- Verify your OpenAI API key is correct
- Check you have sufficient API credits
- Ensure `.env` file is in the project root

### Hotkey not working
- On some systems, you may need to run as administrator
- Try using different key combinations in `config.py`
- Example: `{"ctrl", "alt", "space"}`

## 🚀 Performance Tips

### Speed Up Offline Mode
- Use lighter models: `OFFLINE_MODEL = "distilgpt2"` (faster, less accurate)
- Or more powerful: `OFFLINE_MODEL = "gpt2"` (slower, more accurate)

### Reduce API Costs (Online Mode)
- Use a lower `max_tokens` value in `ai_handler.py`
- Switch to offline mode for quick queries

### Better Voice Recognition
- Reduce `SPEECH_TIMEOUT` for faster input
- Adjust `PHRASE_TIME_LIMIT` for longer queries

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests!

### Ideas for Improvements
- Add weather API integration
- Add email capabilities
- Add calendar integration
- Support for more languages
- Custom wake word detection
- Persistent conversation history

## 📄 License

MIT License - See LICENSE file for details

## ⚠️ Important Notes

### Online Mode
- **API Costs**: OpenAI API calls are not free. Monitor your usage and costs.
- **Privacy**: Your queries are sent to OpenAI's servers
- **Internet Required**: Needs internet connection to work

### Offline Mode
- **Privacy**: All processing happens locally (more private)
- **No Costs**: Completely free to use
- **Slower**: Response time depends on your hardware
- **Limited**: Can't answer complex questions

### Voice Features
- **Voice Recognition**: Audio is processed by Google's servers (online only)
- **Permissions**: The app needs microphone permissions to work
- **Background Access**: On some OS, you may need to grant background execution permissions

## 🔐 Security

- Never commit `.env` file with your API keys
- Keep your OpenAI API key secret
- Use environment variables for sensitive data
- For offline mode: All data stays on your computer

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the configuration settings
3. Verify your mode (online vs offline)
4. Create an issue on GitHub

---

Made with ❤️ by Izo-200812

**Happy Assisting! 🚀**
