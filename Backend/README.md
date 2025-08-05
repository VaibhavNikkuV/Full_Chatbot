# 🔧 Backend Services

Backend infrastructure for the Full_Chatbot project, providing RESTful API services and database management for persistent conversation storage.

## 📁 Backend Structure

```
Backend/
├── README.md           # This file - Backend documentation
├── API_Program/
│   └── main.py        # 🚀 FastAPI REST API server
└── DB/
    └── main.py        # 🗄️ Database setup and schema creation
```

## 🌟 Components Overview

### 🌐 API_Program (`API_Program/main.py`)
**FastAPI REST API Server** - The core backend service that provides HTTP endpoints for the chatbot application.

**Key Features:**
- **RESTful API**: Complete HTTP API for chatbot interactions
- **Database Integration**: Persistent storage of conversations and messages
- **Chatbot Integration**: Seamless connection to the AI chatbot module
- **Conversation Management**: Automatic ID generation and session handling
- **Error Handling**: Comprehensive error management and HTTP status codes
- **JSON Responses**: Structured API responses for frontend integration

### 🗄️ DB (`DB/main.py`)
**Database Setup Script** - Initializes and configures the MySQL database schema.

**Key Features:**
- **Schema Creation**: Sets up required database tables
- **Table Inspection**: Validates database structure
- **Environment Integration**: Uses environment variables for configuration
- **Development Utility**: Easy database setup for development and deployment

## 🚀 API Endpoints

### Base URL: `http://localhost:8000`

| Method | Endpoint | Description | Parameters | Response |
|--------|----------|-------------|------------|----------|
| **GET** | `/` | Root status check | None | `{"status": "Working"}` |
| **GET** | `/health` | Health check | None | `{"status": "Healthy"}` |
| **POST** | `/chat-message` | Send message and get AI response | See below | Chat response with conversation ID |
| **GET** | `/get-conversation-history/{id}` | Retrieve conversation history | `conversation_id` (path) | Message history array |

### Chat Message Endpoint Details

**Endpoint:** `POST /chat-message`

**Parameters:**
```json
{
  "message": "string (required)",           // User message text
  "user_id": "integer (required)",          // User identifier
  "message_id": "string (required)",        // Unique message ID
  "message_count": "integer (required)",    // Message number in conversation
  "conversation_id": "string (optional)"    // Existing conversation ID (empty for new)
}
```

**Response:**
```json
{
  "message": "AI assistant response text",
  "conversation_id": "unique-conversation-id"
}
```

**Workflow:**
1. Receives user message and metadata
2. Calls the AI chatbot module for response generation
3. Stores both user and assistant messages in database
4. Creates conversation record for new conversations
5. Returns AI response with conversation ID

### Conversation History Endpoint Details

**Endpoint:** `GET /get-conversation-history/{conversation_id}`

**Parameters:**
- `conversation_id` (path parameter): The unique conversation identifier

**Response:**
```json
{
  "conversation_id": "conversation-id",
  "message_count": 6,
  "messages": [
    {
      "role": "user",
      "message": "Hello!"
    },
    {
      "role": "assistant", 
      "message": "Hi there, how can I help you?"
    }
  ]
}
```

## 🗄️ Database Schema

### Tables Created by `DB/main.py`

#### `conversation_store`
Tracks conversation metadata and session information.

| Column | Type | Description |
|--------|------|-------------|
| `ID` | INTEGER (Primary Key) | Auto-increment conversation identifier |
| `chat_name` | VARCHAR(60) | Conversation title/name |
| `conv_id` | VARCHAR(20) | Unique conversation ID |
| `user_id` | INTEGER | User identifier |
| `message_count` | INTEGER | Total messages in conversation |
| `created_at` | TIMESTAMP | Conversation creation time |
| `updated_at` | TIMESTAMP | Last conversation update |

#### `message_store`
Stores individual messages with full conversation context.

| Column | Type | Description |
|--------|------|-------------|
| `ID` | INTEGER (Primary Key) | Auto-increment message identifier |
| `role` | VARCHAR | Message role (user/assistant) |
| `conv_id` | VARCHAR(20) | Associated conversation ID |
| `message_no` | INTEGER | Message order in conversation |
| `message_id` | VARCHAR(20) | Unique message identifier |
| `message` | TEXT | Message content |
| `elapsed_time` | INTEGER | Processing time (milliseconds) |
| `Status` | VARCHAR | Message status (Success/Error) |
| `created_at` | TIMESTAMP | Message creation time |
| `updated_at` | TIMESTAMP | Message update time |

## 🛠️ Setup and Configuration

### Prerequisites
- Python 3.8+
- MySQL database server
- OpenAI API key (for chatbot integration)

### Environment Variables

Create a `.env` file in the project root:

```env
# Database Configuration
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=your_mysql_host
DB_PORT=your_mysql_port
DB_NAME=your_database_name
DB_SSL_CA=path/to/ssl/certificate  # Optional

# OpenAI Configuration (for chatbot integration)
OPENAI_API_KEY=your_openai_api_key
```

### Installation

```bash
# From project root
pip install -r requirements.txt
```

### Database Setup

**Step 1: Set up database schema**
```bash
cd Backend/DB
python main.py
```

This will:
- Connect to your MySQL database
- Create `conversation_store` table
- Create `message_store` table  
- Display created tables and their structures

### API Server Startup

**Step 2: Start the FastAPI server**
```bash
cd Backend/API_Program
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Server Options:**
- `--reload`: Auto-reload on code changes (development)
- `--host 0.0.0.0`: Accept connections from any IP
- `--port 8000`: Run on port 8000
- `--workers 4`: Run with multiple workers (production)

### Verify Installation

**Test API endpoints:**
```bash
# Health check
curl http://localhost:8000/

# Health status
curl http://localhost:8000/health

# Send test message
curl -X POST "http://localhost:8000/chat-message" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Hello!",
    "user_id": 1,
    "message_id": "test-msg-001",
    "message_count": 1,
    "conversation_id": ""
  }'
```

## 🔌 Integration Architecture

### Frontend Integration
- **Streamlit Interface**: Connects to API endpoints for testing and user interaction
- **Direct API Calls**: Can be integrated with any HTTP client
- **WebSocket Support**: Ready for real-time communication features

### Chatbot Integration  
- **Module Import**: Imports chatbot functionality from `Chatbot.Main.Chatbot`
- **JSON Communication**: Structured request/response format
- **Error Handling**: Graceful handling of chatbot errors

### Database Integration
- **MySQL Connector**: Direct database operations with connection pooling
- **Transaction Management**: Proper commit/rollback handling
- **Data Persistence**: All conversations and messages stored permanently

## 🛡️ Security Considerations

### Environment Security
- **Credential Management**: All sensitive data in environment variables
- **SSL Support**: Optional SSL certificate configuration for database
- **API Key Protection**: OpenAI API key secured through environment

### Database Security
- **Parameterized Queries**: Prevention of SQL injection attacks
- **Connection Management**: Proper connection opening and closing
- **Error Sanitization**: No sensitive data exposed in error messages

### API Security
- **Input Validation**: Parameter validation and type checking
- **Error Handling**: Structured error responses without data exposure
- **CORS Configuration**: Ready for cross-origin request configuration

## 🚀 Deployment

### Development Deployment
```bash
# Start with auto-reload for development
uvicorn Backend.API_Program.main:app --reload --port 8000
```

### Production Deployment
```bash
# Production server with multiple workers
gunicorn Backend.API_Program.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Docker Deployment
```dockerfile
# Example Dockerfile for containerization
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "Backend.API_Program.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🐛 Troubleshooting

### Common Issues

#### 1. Database Connection Failed
```bash
# Check MySQL service
systemctl status mysql  # Linux
brew services list mysql  # macOS

# Verify credentials
mysql -u $DB_USER -p$DB_PASSWORD -h $DB_HOST -P $DB_PORT $DB_NAME
```

#### 2. FastAPI Import Error
```bash
# Install dependencies
pip install -r requirements.txt

# Check Python path
python -c "import sys; print(sys.path)"
```

#### 3. Chatbot Integration Error
```bash
# Verify chatbot module
python -c "from Chatbot.Main.Chatbot import main"

# Check OpenAI API key
python -c "import os; print(os.getenv('OPENAI_API_KEY')[:10] + '...')"
```

#### 4. Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000

# Kill process
kill -9 <PID>

# Or use different port
uvicorn main:app --port 8001
```

### Debug Mode

**Enable debug logging:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Test individual components:**
```bash
# Test database setup
python Backend/DB/main.py

# Test API server
uvicorn Backend.API_Program.main:app --reload --log-level debug
```

## 📊 Performance Considerations

### Database Optimization
- **Connection Pooling**: Implement connection pooling for production
- **Indexing**: Add indexes on frequently queried columns (`conv_id`, `user_id`)
- **Query Optimization**: Optimize conversation history retrieval queries

### API Performance
- **Async Processing**: Consider async database operations for high load
- **Caching**: Implement response caching for frequently accessed conversations
- **Rate Limiting**: Add rate limiting for production API usage

### Monitoring
- **Health Checks**: Built-in health endpoint for monitoring
- **Logging**: Comprehensive logging for debugging and monitoring
- **Metrics**: Ready for integration with monitoring tools (Prometheus, etc.)

## 🔄 Development Workflow

### Making Changes

1. **Database Changes**: Update `DB/main.py` and run schema migrations
2. **API Changes**: Modify `API_Program/main.py` and test endpoints
3. **Testing**: Use Streamlit interface or direct API calls for testing
4. **Integration**: Test with frontend and chatbot modules

### Testing Strategy

1. **Unit Tests**: Test individual endpoint functions
2. **Integration Tests**: Test complete request/response flow
3. **Database Tests**: Verify data persistence and retrieval
4. **Performance Tests**: Load testing for production readiness

---

## 📋 Module Information

**Part of**: Full_Chatbot Project  
**Version**: 2.0.0  
**Author**: Vaibhav Arya  
**Dependencies**: FastAPI, MySQL Connector, Python-dotenv, OpenAI Integration

**Key Technologies:**
- **FastAPI**: Modern, fast web framework for building APIs
- **MySQL**: Relational database for data persistence  
- **Python-dotenv**: Environment variable management
- **JSON**: Structured data exchange format

For complete project documentation, see the main [README.md](../README.md) file.