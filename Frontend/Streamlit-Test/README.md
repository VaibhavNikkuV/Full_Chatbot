# VibeCoding Streamlit Test Suite 🤖

A comprehensive testing environment for your AI-powered chatbot system built with Streamlit.

## Features

### 💬 Interactive Chatbot
- **Multiple Testing Modes**:
  - FastAPI Backend: Test through your REST API
  - Direct Chatbot: Test the chatbot module directly
  - Both (Comparison): Side-by-side comparison of both methods
- **Beautiful Chat UI**: Modern, responsive chat interface with message bubbles
- **Conversation Management**: Start new conversations, clear chat history
- **Real-time Testing**: Instant feedback and error handling

### 🔍 API Testing
- **Endpoint Testing**: Test all FastAPI endpoints individually
- **Parameter Configuration**: Customize request parameters
- **Response Inspection**: View detailed API responses and status codes
- **Error Handling**: Clear error messages and debugging information

### 📊 Database Testing
- **Connection Testing**: Verify database connectivity
- **Table Inspection**: View available database tables
- **Environment Variables**: Check required environment variables
- **Query Testing**: Test database operations

### 📈 Analytics & Monitoring
- **Real-time Metrics**: Track chat sessions, API status, and system health
- **Message Statistics**: Analyze conversation patterns and message lengths
- **Export Functionality**: Download chat history as JSON
- **Session Management**: Monitor current session details

## Quick Start

### 1. Install Dependencies
```bash
# From the project root directory
pip install -r requirements.txt
```

### 2. Set Up Environment Variables
Create a `.env` file in your project root with the following variables:
```env
# Database Configuration
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
DB_NAME=your_db_name

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key
```

### 3. Start the FastAPI Backend (Optional)
```bash
# From the Backend/API_Program directory
cd Backend/API_Program
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Launch the Streamlit App
```bash
# From the Frontend/Streamlit-Test directory
cd Frontend/Streamlit-Test
streamlit run test.py
```

The app will open in your browser at `http://localhost:8501`

## Usage Guide

### Configuration (Sidebar)
1. **API Settings**: Configure your FastAPI backend URL (default: `http://localhost:8000`)
2. **Test Connection**: Verify API connectivity before testing
3. **Chat Settings**: Set user ID and manage conversations
4. **Conversation Controls**: Start new conversations or clear chat history

### Testing Modes

#### FastAPI Backend Mode
- Tests the complete system through your REST API
- Includes database storage and full conversation history
- Best for end-to-end testing

#### Direct Chatbot Mode
- Tests the chatbot module directly
- Bypasses the API layer
- Useful for isolating chatbot functionality

#### Comparison Mode
- Runs both methods simultaneously
- Shows side-by-side responses
- Perfect for debugging discrepancies

### API Testing Tab
- **Root Endpoint**: Test basic API connectivity
- **Chat Message**: Test the main chat functionality with custom parameters
- **Conversation History**: Retrieve and display conversation history

### Database Testing Tab
- **Connection Test**: Verify database connectivity
- **Show Tables**: List available database tables
- **Environment Check**: Validate required environment variables

### Analytics Tab
- **System Metrics**: Monitor chat sessions, API status, and session time
- **Message Statistics**: Analyze conversation patterns
- **Export Feature**: Download chat history for analysis

## Troubleshooting

### Common Issues

1. **API Connection Failed**
   - Ensure FastAPI backend is running on the correct port
   - Check the API base URL in the sidebar
   - Verify network connectivity

2. **Database Connection Error**
   - Check environment variables in `.env` file
   - Verify database server is running
   - Ensure database credentials are correct

3. **OpenAI API Error**
   - Verify `OPENAI_API_KEY` in environment variables
   - Check API key validity and quota
   - Ensure internet connectivity

4. **Import Errors**
   - Install all dependencies: `pip install -r requirements.txt`
   - Ensure you're running from the correct directory
   - Check Python path and module imports

### Debug Tips

1. **Use the Direct Chatbot Mode** to isolate issues with the chatbot itself
2. **Check the Database Tests Tab** to verify all environment variables
3. **Monitor the Analytics Tab** for real-time system status
4. **Use Comparison Mode** to identify differences between API and direct calls

## File Structure

```
Frontend/Streamlit-Test/
├── test.py           # Main Streamlit application
└── README.md         # This documentation
```

## Dependencies

- `streamlit>=1.28.0` - Web application framework
- `requests>=2.31.0` - HTTP requests for API testing
- `python-dotenv>=1.0.0` - Environment variable management
- Other dependencies from the main project

## Features in Detail

### Beautiful UI Components
- **Custom CSS Styling**: Modern gradient headers and styled components
- **Responsive Design**: Works well on different screen sizes
- **Intuitive Navigation**: Tabbed interface for different testing modes
- **Status Indicators**: Clear success/error states with color coding

### Advanced Testing Features
- **Conversation Persistence**: Maintains conversation context across interactions
- **Error Handling**: Comprehensive error catching and user-friendly messages
- **Real-time Updates**: Live status updates and metrics
- **Export Capabilities**: Download conversation history for analysis

### Integration Testing
- **Full Stack Testing**: Test the complete system from UI to database
- **Component Isolation**: Test individual components separately
- **Performance Monitoring**: Track response times and system health
- **Data Validation**: Verify data flow through all system layers

## Contributing

To extend the testing suite:

1. **Add New Test Cases**: Extend the testing tabs with additional functionality
2. **Enhance UI**: Improve the visual design and user experience
3. **Add Metrics**: Include additional monitoring and analytics features
4. **Extend API Testing**: Add tests for new endpoints as they're developed

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all dependencies are installed correctly
3. Ensure environment variables are properly configured
4. Test individual components using the provided testing modes

---
**Built with ❤️ using Streamlit and modern web technologies** 