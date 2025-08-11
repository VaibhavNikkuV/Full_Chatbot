# 🤖 OpenAI Chatbot Project

Core AI chatbot implementations for the Full_Chatbot project, featuring both simple CLI interface and database-integrated chatbot with persistent conversation storage.

## 📁 Module Structure

```
Chatbot/
├── README.md                # This file - Module documentation
├── Main/
│   └── Chatbot.py          # 🚀 Database-integrated chatbot (production)
└── Test/
    └── main.py             # Simple CLI chatbot (development/testing)
```

## 🌟 Features

### Main Implementation (`Main/Chatbot.py`)
- **GPT-4o-mini Integration**: Uses OpenAI's efficient and cost-effective model
- **Database Persistence**: Stores conversations and messages in MySQL database
- **Conversation Management**: Automatic conversation ID generation and retrieval
- **Message History**: Maintains complete conversation context from database
- **JSON API Response**: Returns structured JSON responses for API integration
- **Error Handling**: Comprehensive error handling with graceful degradation
- **Environment Security**: Secure database and API key management

### Test Implementation (`Test/main.py`)
- **Simple CLI Interface**: Direct command-line chatbot interaction
- **In-Memory Conversation**: Maintains conversation history during session
- **Interactive Commands**: Built-in commands for conversation management
- **Lightweight Setup**: Minimal dependencies and configuration
- **Development Ready**: Perfect for testing and development

## 🛠️ Implementation Comparison

| Feature | Main/Chatbot.py | Test/main.py |
|---------|----------------|---------------|
| **Database Storage** | ✅ MySQL persistent storage | ❌ Session-only memory |
| **API Integration** | ✅ JSON responses for FastAPI | ❌ Direct console output |
| **Conversation History** | ✅ Persistent across sessions | ❌ Lost on restart |
| **Conversation IDs** | ✅ Auto-generated unique IDs | ❌ No ID management |
| **Multi-User Support** | ✅ User ID and message tracking | ❌ Single session only |
| **Setup Complexity** | 🔶 Requires database setup | ✅ Minimal setup |
| **Use Case** | Production API backend | Development and testing |

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- MySQL database (for Main implementation)
- OpenAI API key

### Environment Configuration

Create a `.env` file in the project root directory:

```env
# OpenAI Configuration (Required for both implementations)
OPENAI_API_KEY=your_openai_api_key

# Database Configuration (Required only for Main implementation)
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=your_mysql_host
DB_PORT=your_mysql_port
DB_NAME=your_database_name
DB_SSL_CA=path/to/ssl/certificate  # Optional
```

### Installation

From the project root directory:

```bash
# Install all dependencies
pip install -r requirements.txt
```

## 💬 Usage Guide

### Option 1: Production Chatbot (Main/Chatbot.py)

**For API Integration:**
```python
from Chatbot.Main.Chatbot import main as chatbot_main

# Send a message
response = chatbot_main("Hello, how are you?", conversation_id="")
print(response)  # Returns JSON string with message and conversation_id
```

**Direct Usage:**
```python
from Chatbot.Main.Chatbot import OpenAIChatbot

chatbot = OpenAIChatbot()
response = chatbot.chat("Hello!", "")
print(response)  # JSON response
```

### Option 2: Simple CLI Chatbot (Test/main.py)

```bash
cd Chatbot/Test
python main.py
```

**Available Commands:**
- `quit`, `exit`, `bye` - End the conversation
- `clear` - Reset conversation history
- Regular text - Chat with the AI

### Example CLI Session

```
🤖 OpenAI Chatbot (GPT-4o-mini)
========================================
Type 'quit', 'exit', or 'bye' to end the conversation.
Type 'clear' to clear conversation history.
========================================

You: Hello! How are you today?

🤖 Assistant: Hello! I'm doing great, thank you for asking! I'm here and ready to help you with any questions or tasks you might have. How are you doing today?

You: clear

🤖 Conversation history cleared!

You: quit

🤖 Goodbye! Have a great day!
```

## 🔧 Technical Implementation

### Main Implementation Details

#### OpenAIChatbot Class
- **Database Integration**: Connects to MySQL for conversation storage
- **Conversation Management**: Handles conversation ID generation and retrieval
- **Message Processing**: Stores both user and assistant messages
- **API Response Format**: Returns structured JSON responses

#### Key Methods
- `get_response(user_message, conversation_id)`: Core chat functionality
- `chat(query, conversation_id)`: Public interface with error handling
- `main(query, conversation_id)`: Entry point for external usage

#### Database Integration
- Retrieves conversation history from `message_store` table
- Automatically generates conversation IDs for new conversations
- Maintains message order and conversation continuity

### Test Implementation Details

#### OpenAIChatbot Class (Simple)
- **In-Memory Storage**: Conversation history stored in class instance
- **Interactive Loop**: Continuous chat interface with command processing
- **Direct Output**: Immediate console output for responses

## 🔌 Integration with Full_Chatbot Project

### Backend API Integration
The Main implementation is used by the FastAPI backend (`Backend/API_Program/main.py`):

```python
from Chatbot import main as chatbot_main
response = chatbot_main(message, conversation_id)
```

### Frontend Integration
The Streamlit frontend can test both implementations:
- **FastAPI Backend Mode**: Uses Main implementation through API
- **Direct Chatbot Mode**: Uses Main implementation directly
- **Comparison Mode**: Shows responses from both methods

## 🛡️ Security Considerations

### Environment Variables
- API keys stored securely in `.env` file
- Database credentials managed through environment variables
- No hardcoded secrets in source code

### Error Handling
- Graceful API failure handling
- Database connection error management
- JSON parsing error prevention
- User input validation

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