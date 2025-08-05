# 🤖 Full_Chatbot

A comprehensive full-stack AI-powered chatbot application built with OpenAI's GPT-4o-mini, featuring persistent conversation storage, RESTful API architecture, and a modern testing interface.

## 🌟 Features

### 🧠 Core AI Capabilities
- **OpenAI GPT-4o-mini Integration**: Efficient and cost-effective AI model
- **Persistent Conversation Memory**: All conversations stored in MySQL database
- **Context Retention**: Maintains conversation history across sessions
- **Unique Conversation IDs**: Automatic generation and management

### 🔧 Architecture Components
- **FastAPI Backend**: RESTful API with comprehensive endpoints
- **MySQL Database**: Persistent storage for conversations and messages
- **Streamlit Frontend**: Modern web interface with testing capabilities
- **Modular Design**: Separated concerns with clear component boundaries

### 🎯 Testing & Monitoring
- **Multi-Mode Testing**: API, Direct, and Comparison testing modes
- **Real-time Analytics**: Conversation metrics and system monitoring
- **Database Testing**: Connection verification and table inspection
- **Export Functionality**: Download conversation history as JSON

## 📁 Project Structure

```
Full_Chatbot/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── .env                        # Environment variables (create this)
├── Backend/                    # Backend services
│   ├── API_Program/
│   │   └── main.py            # FastAPI server with REST endpoints
│   └── DB/
│       └── main.py            # Database schema and setup
├── Chatbot/                   # Core chatbot implementation
│   ├── Main/
│   │   └── Chatbot.py         # Main chatbot with DB integration
│   ├── Test/
│   │   └── main.py            # Simple CLI chatbot interface
│   └── README.md              # Chatbot-specific documentation
└── Frontend/                  # Frontend interfaces
    └── Streamlit-Test/
        ├── test.py            # Comprehensive testing dashboard
        └── README.md          # Frontend documentation
```

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8+
- MySQL database server
- OpenAI API key

### 2. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd Full_Chatbot

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration

Create a `.env` file in the project root:

```env
# Database Configuration
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=your_mysql_host
DB_PORT=your_mysql_port
DB_NAME=your_database_name
DB_SSL_CA=path/to/ssl/certificate  # Optional

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key
```

### 4. Database Setup

```bash
# Set up database tables
cd Backend/DB
python main.py
```

### 5. Start the Application

#### Option A: Full Stack (Recommended)

**Terminal 1 - Start Backend API:**
```bash
cd Backend/API_Program
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Start Frontend Interface:**
```bash
cd Frontend/Streamlit-Test
streamlit run test.py
```

#### Option B: Direct Chatbot (CLI)
```bash
cd Chatbot/Test
python main.py
```

## 🎮 Usage Guide

### 🌐 Web Interface (Streamlit)

Access the comprehensive testing dashboard at `http://localhost:8501`

#### Available Tabs:

1. **💬 Chatbot Tab**
   - **FastAPI Backend Mode**: Full-stack testing through REST API
   - **Direct Chatbot Mode**: Direct interaction with chatbot module
   - **Comparison Mode**: Side-by-side comparison of both methods

2. **🔍 API Testing Tab**
   - Test individual API endpoints
   - Customize request parameters
   - View detailed responses and status codes

3. **📊 Database Tests Tab**
   - Verify database connectivity
   - Inspect database tables
   - Check environment variables

4. **📈 Analytics Tab**
   - Real-time system metrics
   - Conversation statistics
   - Export chat history

### 🖥️ Command Line Interface

```bash
cd Chatbot/Test
python main.py
```

**Available Commands:**
- `quit`, `exit`, `bye` - End conversation
- `clear` - Reset conversation history
- Regular text - Chat with the AI

## 🛠️ API Endpoints

### Base URL: `http://localhost:8000`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check - returns system status |
| GET | `/health` | Detailed health information |
| POST | `/chat-message` | Send message and get AI response |
| GET | `/get-conversation-history/{conversation_id}` | Retrieve conversation history |

#### Chat Message Endpoint
```http
POST /chat-message
Parameters:
  - message: str (required) - User message
  - user_id: int (required) - User identifier
  - message_id: str (required) - Unique message ID
  - message_count: int (required) - Message count in conversation
  - conversation_id: str (optional) - Existing conversation ID
```

## 🗄️ Database Schema

### Tables

#### `conversation_store`
- `ID` (Primary Key) - Auto-increment conversation identifier
- `chat_name` - Conversation title
- `conv_id` - Unique conversation ID
- `user_id` - User identifier
- `message_count` - Number of messages in conversation
- `created_at` / `updated_at` - Timestamps

#### `message_store`
- `ID` (Primary Key) - Auto-increment message identifier
- `role` - Message role (user/assistant)
- `conv_id` - Associated conversation ID
- `message_no` - Message order in conversation
- `message_id` - Unique message identifier
- `message` - Message content
- `elapsed_time` - Processing time
- `Status` - Message status
- `created_at` / `updated_at` - Timestamps

## 🧪 Testing

### Automated Testing
The Streamlit interface provides comprehensive testing capabilities:

1. **API Integration Tests** - Verify all endpoints
2. **Database Connection Tests** - Ensure data persistence
3. **End-to-End Testing** - Complete user journey validation
4. **Performance Monitoring** - Response time tracking

### Manual Testing
Use the comparison mode to validate consistency between:
- Direct chatbot responses
- API-mediated responses
- Database-stored conversation history

## 📦 Dependencies

### Core Dependencies
```txt
openai>=1.0.0              # OpenAI API client
python-dotenv>=1.0.0       # Environment variable management
fastapi>=0.105.0           # Web framework for API
uvicorn>=0.25.0            # ASGI server
mysql-connector-python>=9.0.0  # MySQL database connector
```

### Frontend & Testing
```txt
streamlit>=1.28.0          # Web interface framework
requests>=2.31.0           # HTTP client for API testing
PyMySQL>=1.1.0             # Additional MySQL support
python-multipart>=0.0.9    # Form data handling
passlib>=1.7.4             # Password hashing utilities
```

## 🔒 Security Considerations

- API keys stored in environment variables (not in code)
- Database credentials managed through `.env` file
- SQL injection prevention through parameterized queries
- Error handling prevents sensitive information exposure

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Failed**
   ```bash
   # Check MySQL service status
   systemctl status mysql  # Linux
   brew services list mysql  # macOS
   
   # Verify credentials in .env file
   ```

2. **OpenAI API Error**
   ```bash
   # Verify API key validity
   # Check account quota and billing
   # Ensure internet connectivity
   ```

3. **FastAPI Import Errors**
   ```bash
   # Install all dependencies
   pip install -r requirements.txt
   
   # Check Python path
   echo $PYTHONPATH
   ```

4. **Streamlit Won't Start**
   ```bash
   # Reinstall Streamlit
   pip uninstall streamlit
   pip install streamlit>=1.28.0
   
   # Clear Streamlit cache
   streamlit cache clear
   ```

## 🚀 Deployment

### Local Development
Follow the Quick Start guide above.

### Production Deployment
1. **Backend**: Deploy FastAPI using Gunicorn or similar WSGI server
2. **Database**: Use managed MySQL service (AWS RDS, Google Cloud SQL)
3. **Frontend**: Deploy Streamlit app using Streamlit Cloud or containerization
4. **Environment**: Use secure secret management for production credentials

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source. Please check the repository for license details.

## 👨‍💻 Author

**Vaibhav Arya**

## 🔄 Version History

- **v1.0.0** - Initial release with core functionality
  - OpenAI GPT-4o-mini integration
  - FastAPI backend with REST endpoints
  - MySQL database persistence
  - Streamlit testing interface
  - Comprehensive documentation

---

## 🆘 Support

For issues, questions, or contributions:

1. Check the troubleshooting section above
2. Review the component-specific README files
3. Test individual components using the Streamlit interface
4. Create an issue in the repository

**Built with ❤️ using OpenAI, FastAPI, Streamlit, and MySQL**