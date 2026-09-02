# 🤖 Personal Assistant Bot

An always-active AI assistant application that responds to your commands via voice or text. Similar to Siri, it runs in the background and can be activated with a hotkey.

## ✨ Features

- 🎤 **Voice Recognition** - Speak commands naturally
- 🔊 **Text-to-Speech** - Hear responses from the bot
- ⌨️ **Hotkey Activation** - Press `Ctrl+Shift+A` to activate
- 🧠 **AI Powered** - Uses OpenAI's GPT-3.5 for intelligent responses
- 💬 **Conversation Memory** - Maintains context across interactions
- 🔧 **Configurable** - Easy customization via config.py

## 📋 Requirements

- Python 3.7+
- Microphone for voice input
- Speaker for voice output
- OpenAI API key
- Windows, macOS, or Linux

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

### 4. Configure OpenAI API Key
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

1. **Start the bot:**
   ```bash
   python main.py
   ```

2. **Activate the bot:**
   - Press `Ctrl+Shift+A` (or configured hotkey)
   - The bot will say "Assistant is now active!"

3. **Give a command:**
   - Speak your command or type it
   - Wait for the response

4. **Examples:**
   - "What's the weather?"
   - "Tell me a joke"
   - "What is Python?"
   - "How do I write a function?"

## ⚙️ Configuration

Edit `config.py` to customize:

```python
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
```

## 📁 Project Structure

```
personal-assistant-bot/
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── voice_handler.py       # Speech recognition & TTS
├── ai_handler.py          # OpenAI API integration
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
  for i, mic in enumerate(sr.Microphone.list_microphone_indexes()):
      print(f"{i}: {mic}")
  ```

### Voice output not working
- Ensure speakers are enabled
- Check volume levels
- Install audio drivers for your OS

### API Key errors
- Verify your OpenAI API key is correct
- Check you have sufficient API credits
- Ensure `.env` file is in the project root

### Hotkey not working
- On some systems, you may need to run as administrator
- Try using different key combinations in `config.py`

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests!

## 📄 License

MIT License - See LICENSE file for details

## ⚠️ Important Notes

- **API Costs**: OpenAI API calls are not free. Monitor your usage and costs.
- **Privacy**: Voice data is sent to Google's servers for speech recognition
- **Permissions**: The app needs microphone permissions to work
- **Background Access**: On some OS, you may need to grant background execution permissions

## 🔐 Security

- Never commit `.env` file with your API keys
- Keep your OpenAI API key secret
- Use environment variables for sensitive data

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the configuration settings
3. Create an issue on GitHub

---

Made with ❤️ by Izo-200812
