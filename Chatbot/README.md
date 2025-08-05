# 🤖 OpenAI Chatbot Module

A simple yet powerful chatbot implementation using OpenAI's GPT-4o-mini model with conversation memory and interactive commands.

## 📁 Module Structure

```
Chatbot/
├── README.md           # This file - Project documentation
├── requirements.txt    # Python dependencies for the entire project
├── Main/              # Main chatbot implementation directory
│   ├── main.py
│   ├── pyproject.toml
│   └── README.md
└── Test/              # Test chatbot implementation directory
    ├── main.py        # 🚀 Current working chatbot implementation
    ├── pyproject.toml # Project configuration with dependencies
    └── README.md
```

## 🌟 Features

### Current Implementation (Test Directory)

- **GPT-4o-mini Integration**: Uses OpenAI's efficient and cost-effective 4o-mini model
- **Environment Variables**: Securely loads API key from `.env` file using python-dotenv
- **Conversation Memory**: Maintains context throughout the entire chat session
- **Interactive Commands**:
  - `quit`, `exit`, or `bye` - End the conversation gracefully
  - `clear` - Reset conversation history and start fresh
- **Error Handling**: Robust error handling for API failures and user interruptions
- **User-Friendly Interface**: Clean chat interface with emojis and clear prompts

## 🛠️ Dependencies

The project uses the following Python packages:

```txt
openai>=1.0.0          # OpenAI API client
python-dotenv>=1.0.0   # Environment variable management
```

## 🚀 Setup Instructions

### 1. Install Dependencies

Navigate to the Test directory and install the required packages:

```bash
cd Chatbot/Test
pip install -e .
```

Or install from the main requirements file:

```bash
cd Chatbot
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the `Chatbot/Test/` directory:

```bash
# Navigate to Test directory
cd Test

# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=your-actual-openai-api-key-here" > .env
```

**Important**: Replace `your-actual-openai-api-key-here` with your real OpenAI API key from [OpenAI Platform](https://platform.openai.com/).

### 3. Run the Chatbot

```bash
python main.py
```

## 💬 How to Use

1. **Start the Chatbot**: Run `python main.py` in the Test directory
2. **Chat Naturally**: Type any message and press Enter
3. **Conversation Context**: The bot remembers your entire conversation
4. **Special Commands**:
   - Type `clear` to start a fresh conversation
   - Type `quit`, `exit`, or `bye` to end the session
5. **Exit Gracefully**: Use Ctrl+C or the exit commands

### Example Conversation

```
🤖 OpenAI Chatbot (GPT-4o-mini)
========================================
Type 'quit', 'exit', or 'bye' to end the conversation.
Type 'clear' to clear conversation history.
========================================

You: Hello! How are you today?

🤖 Assistant: Hello! I'm doing great, thank you for asking! I'm here and ready to help you with any questions or tasks you might have. How are you doing today?

You: What's the weather like?

🤖 Assistant: I don't have access to real-time weather data, so I can't tell you the current weather conditions. To get accurate weather information, I'd recommend:

1. Checking a weather app on your phone
2. Visiting weather.com or weather.gov
3. Asking a voice assistant with internet access
4. Looking outside your window!

Is there anything else I can help you with?

You: quit

🤖 Goodbye! Have a great day!
```

## 🔧 Technical Implementation

### Core Components

1. **OpenAIChatbot Class**: Main chatbot implementation
   - Initializes OpenAI client with API key validation
   - Manages conversation history
   - Handles API requests and responses

2. **Environment Management**: Uses python-dotenv for secure API key loading

3. **Conversation Flow**: Implements a continuous chat loop with command processing

### API Configuration

- **Model**: `gpt-4o-mini` (OpenAI's efficient model)
- **Max Tokens**: 500 per response
- **Temperature**: 0.7 (balanced creativity and coherence)
- **System Prompt**: "You are a helpful assistant. Be concise and friendly."

## 🛡️ Security Notes

- API keys are stored in `.env` files (not tracked by git)
- Error handling prevents API key exposure
- Graceful degradation on API failures

## 🐛 Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY not found"**
   - Ensure `.env` file exists in the Test directory
   - Verify your API key is correct and active
   - Check that the `.env` file format is correct

2. **Import Errors**
   - Run `pip install -r requirements.txt` to install dependencies
   - Ensure you're in the correct directory

3. **API Errors**
   - Check your OpenAI account has sufficient credits
   - Verify your API key has the correct permissions
   - Check your internet connection

## 📝 Development Notes

- Built with Python 3.13+
- Uses OpenAI Python SDK v1.0+
- Implements conversation memory for context retention
- Designed for easy extension and modification

## 🔄 Future Enhancements

Potential improvements for future versions:
- GUI interface using tkinter or streamlit
- Voice input/output capabilities
- Custom system prompts configuration
- Chat history persistence
- Multiple model support
- Plugin system for extended functionality

---

**Last Updated**: Created with OpenAI GPT-4o-mini integration
**Version**: 1.0.0
**Author**: Vaibhav
