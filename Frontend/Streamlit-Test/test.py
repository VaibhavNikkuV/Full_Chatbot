import streamlit as st
import requests
import json
import sys
import os
from datetime import datetime
from dotenv import load_dotenv
import mysql.connector
import string
import random

# Load environment variables
load_dotenv()


def generate_random_id():
    chars = string.ascii_lowercase + string.digits
    parts = [8, 4]
    result = '-'.join(''.join(random.choices(chars, k=p)) for p in parts)
    return result


# Add the project root to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))


def db_connection():
    db = mysql.connector.connect(
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        database = os.getenv("DB_NAME"),
        ssl_ca = os.getenv("DB_SSL_CA")
    )
    return db


# Page configuration
st.set_page_config(
    page_title="VibeCoding Test Suite",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .chat-container {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .user-message {
        background: #007bff;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 15px 15px 5px 15px;
        margin: 0.5rem 0;
        margin-left: 20%;
        text-align: right;
    }
    
    .bot-message {
        background: #e9ecef;
        color: #333;
        padding: 0.5rem 1rem;
        border-radius: 15px 15px 15px 5px;
        margin: 0.5rem 0;
        margin-right: 20%;
    }
    
    .status-success {
        background: #d4edda;
        color: #155724;
        padding: 0.5rem;
        border-radius: 5px;
        border-left: 4px solid #28a745;
    }
    
    .status-error {
        background: #f8d7da;
        color: #721c24;
        padding: 0.5rem;
        border-radius: 5px;
        border-left: 4px solid #dc3545;
    }
    
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🤖 VibeCoding Test Suite</h1>
    <p>Comprehensive testing environment for your AI-powered chatbot system</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'conversation_id' not in st.session_state:
    st.session_state.conversation_id = None
if 'api_base_url' not in st.session_state:
    st.session_state.api_base_url = "http://localhost:8000"

# Sidebar for configuration and controls
with st.sidebar:
    st.header("🔧 Configuration")
    
    # API Configuration
    st.subheader("API Settings")
    api_base_url = st.text_input(
        "FastAPI Base URL", 
        value=st.session_state.api_base_url,
        help="Base URL for your FastAPI backend"
    )
    st.session_state.api_base_url = api_base_url
    
    # Test API Connection
    if st.button("🔍 Test API Connection"):
        try:
            response = requests.get(f"{api_base_url}/", timeout=5)
            if response.status_code == 200:
                st.success("✅ API Connection Successful!")
                st.json(response.json())
            else:
                st.error(f"❌ API returned status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Connection failed: {str(e)}")
    
    st.divider()
    
    # Chat Configuration
    st.subheader("Chat Settings")
    user_id = st.number_input("User ID", value=1, min_value=1)
    
    # Conversation controls
    if st.button("🆕 New Conversation"):
        st.session_state.messages = []
        st.session_state.conversation_id = None
        st.rerun()
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # Display current conversation ID
    if st.session_state.conversation_id:
        st.info(f"💬 Conversation ID: {st.session_state.conversation_id[:8]}...")

# Main content area with tabs
tab1, tab2, tab3, tab4 = st.tabs(["💬 Chatbot", "🔍 API Testing", "📊 Database Tests", "📈 Analytics"])

with tab1:
    st.header("Interactive Chatbot")
    
    # Testing mode selection
    test_mode = st.radio(
        "Select Testing Mode:",
        ["FastAPI Backend", "Direct Chatbot", "Both (Comparison)"],
        horizontal=True
    )
    
    # Chat interface
    chat_container = st.container()
    
    with chat_container:
        # Display conversation history
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"""
                <div class="user-message">
                    👤 {message["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="bot-message">
                    🤖 {message["content"]}
                </div>
                """, unsafe_allow_html=True)
    
    # Chat input
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": user_input})
        # print("type of user input: ", type(user_input))
        
        # Generate message ID
        message_id = generate_random_id()
        message_count = len([msg for msg in st.session_state.messages if msg["role"] == "user"])
        
        with st.spinner("🤖 Thinking..."):
            if test_mode == "FastAPI Backend":
                try:
                    # Call FastAPI backend
                    response = requests.post(f"{api_base_url}/chat-message", params={
                        "message": user_input,
                        "user_id": user_id,
                        "message_id": message_id,
                        "message_count": message_count,
                        "conversation_id": st.session_state.conversation_id
                    })
                    
                    if response.status_code == 200:
                        responseFormatted = response.json()
                        bot_response = responseFormatted.get("message")
                        st.session_state.conversation_id = responseFormatted.get("conversation_id")
                        st.session_state.messages.append({"role": "assistant", "content": bot_response})
                        
                        # Update conversation ID if it's a new conversation
                        if not st.session_state.conversation_id:
                            # Extract conversation ID from backend response or generate one
                            st.session_state.conversation_id = responseFormatted.get("conversation_id")
                    else:
                        error_msg = f"API Error: {response.status_code} - {response.text}"
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})
                
                except Exception as e:
                    error_msg = f"Connection Error: {str(e)}"
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
            
            elif test_mode == "Direct Chatbot":
                try:
                    # Import and use chatbot directly
                    from Chatbot.Main.Chatbot import main as chatbot_main
                    
                    bot_response = chatbot_main(user_input, st.session_state.conversation_id)
                    st.session_state.messages.append({"role": "assistant", "content": bot_response})
                    
                    if not st.session_state.conversation_id:
                        st.session_state.conversation_id = generate_random_id()
                
                except Exception as e:
                    error_msg = f"Chatbot Error: {str(e)}"
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
            
            elif test_mode == "Both (Comparison)":
                col1, col2 = st.columns(2)
                
                # FastAPI response
                with col1:
                    st.subheader("FastAPI Response")
                    try:
                        response = requests.post(f"{api_base_url}/chat-message", params={
                            "message": user_input,
                            "user_id": user_id,
                            "message_id": message_id,
                            "message_count": message_count,
                            "conversation_id": st.session_state.conversation_id
                        })
                        
                        if response.status_code == 200:
                            api_response = response.json()["message"]
                            st.success("✅ API Success")
                        else:
                            api_response = f"API Error: {response.status_code}"
                            st.error("❌ API Error")
                    except Exception as e:
                        api_response = f"Connection Error: {str(e)}"
                        st.error("❌ Connection Error")
                    
                    st.write(api_response)
                
                # Direct chatbot response
                with col2:
                    st.subheader("Direct Chatbot Response")
                    try:
                        from Chatbot.Main.Chatbot import main as chatbot_main
                        
                        direct_response = chatbot_main(user_input, st.session_state.conversation_id)
                        st.success("✅ Direct Success")
                        st.write(direct_response)
                    except Exception as e:
                        direct_response = f"Chatbot Error: {str(e)}"
                        st.error("❌ Chatbot Error")
                        st.write(direct_response)
        
        st.rerun()

with tab2:
    st.header("API Endpoint Testing")
    
    # Root endpoint test
    st.subheader("🏠 Root Endpoint Test")
    if st.button("Test GET /"):
        try:
            response = requests.get(f"{api_base_url}/")
            if response.status_code == 200:
                st.success(f"✅ Status: {response.status_code}")
                st.json(response.json())
            else:
                st.error(f"❌ Status: {response.status_code}")
                st.text(response.text)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    
    st.divider()
    
    # Chat message endpoint test
    st.subheader("💬 Chat Message Endpoint Test")
    
    col1, col2 = st.columns(2)
    with col1:
        test_message = st.text_input("Test Message", "Hello, how are you?")
        test_user_id = st.number_input("Test User ID", value=1)
    
    with col2:
        test_message_id = st.text_input("Message ID", generate_random_id())
        test_conv_id = st.text_input("Conversation ID (optional)", "")
    
    if st.button("Test POST /chat-message"):
        try:
            params = {
                "message": test_message,
                "user_id": test_user_id,
                "message_id": test_message_id,
                "message_count": 1,
                "conversation_id": test_conv_id if test_conv_id else None
            }
            
            response = requests.post(f"{api_base_url}/chat-message", params=params)
            
            if response.status_code == 200:
                st.success(f"✅ Status: {response.status_code}")
                st.json(response.json())
            else:
                st.error(f"❌ Status: {response.status_code}")
                st.text(response.text)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    
    st.divider()
    
    # Conversation history endpoint test
    st.subheader("📜 Conversation History Test")
    
    history_conv_id = st.text_input("Conversation ID for History", 
                                   value=st.session_state.conversation_id if st.session_state.conversation_id else "")
    
    if st.button("Test GET /get-conversation-history"):
        if history_conv_id:
            try:
                response = requests.get(f"{api_base_url}/get-conversation-history/{history_conv_id}")
                
                if response.status_code == 200:
                    st.success(f"✅ Status: {response.status_code}")
                    history_data = response
                    for msg in history_data:
                        st.text(msg)
                else:
                    st.error(f"❌ Status: {response.status_code}")
                    st.text(response.text)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("Please enter a conversation ID")

with tab3:
    st.header("Database Connection Tests")
    
    # Test database connection
    st.subheader("🗄️ Database Connection Test")
    
    if st.button("Test Database Connection"):
        try:
            db = db_connection()
            cursor = db.cursor()
            
            # Test query
            cursor.execute("SELECT 1 as test")
            result = cursor.fetchone()
            
            if result:
                st.success("✅ Database connection successful!")
                st.info(f"Test query result: {result}")
            
        except Exception as e:
            st.error(f"❌ Database connection failed: {str(e)}")
    
    st.divider()
    
    # Show tables
    st.subheader("📋 Database Tables")
    
    if st.button("Show Tables"):
        try:
            db = db_connection()
            cursor = db.cursor()
            
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            
            if tables:
                st.success("✅ Tables found:")
                for table in tables:
                    st.text(f"📊 {table[0]}")
            else:
                st.warning("No tables found")
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    
    st.divider()
    
    # Environment variables check
    st.subheader("🔐 Environment Variables Check")
    
    if st.button("Check Environment Variables"):
        env_vars = ['DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT', 'DB_NAME', 'OPENAI_API_KEY']
        
        for var in env_vars:
            value = os.getenv(var)
            if value:
                st.success(f"✅ {var}: {'*' * len(value[:3]) + '...' if len(value) > 3 else '***'}")
            else:
                st.error(f"❌ {var}: Not set")

with tab4:
    st.header("Analytics & Monitoring")
    
    # System status
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>💬 Chat Sessions</h3>
            <h2>""" + str(len(st.session_state.messages)) + """</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🔄 API Status</h3>
            <h2>""" + ("🟢 Online" if api_base_url else "🔴 Offline") + """</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>⏰ Session Time</h3>
            <h2>""" + str(datetime.now().strftime("%H:%M")) + """</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Message statistics
    if st.session_state.messages:
        st.subheader("📊 Message Statistics")
        
        user_messages = [msg for msg in st.session_state.messages if msg["role"] == "user"]
        bot_messages = [msg for msg in st.session_state.messages if msg["role"] == "assistant"]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("User Messages", len(user_messages))
            st.metric("Bot Messages", len(bot_messages))
        
        with col2:
            avg_user_length = sum(len(msg["content"]) for msg in user_messages) / len(user_messages) if user_messages else 0
            avg_bot_length = sum(len(msg["content"]) for msg in bot_messages) / len(bot_messages) if bot_messages else 0
            
            st.metric("Avg User Message Length", f"{avg_user_length:.1f}")
            st.metric("Avg Bot Message Length", f"{avg_bot_length:.1f}")
    
    st.divider()
    
    # Export chat history
    st.subheader("💾 Export Chat History")
    
    if st.button("Download Chat History"):
        if st.session_state.messages:
            chat_export = {
                "conversation_id": st.session_state.conversation_id,
                "timestamp": datetime.now().isoformat(),
                "messages": st.session_state.messages
            }
            
            st.download_button(
                label="Download JSON",
                data=json.dumps(chat_export, indent=2),
                file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
        else:
            st.warning("No chat history to export")

# Footer
st.markdown("""
---
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>🚀 VibeCoding Test Suite | Built with Streamlit & ❤️</p>
</div>
""", unsafe_allow_html=True)
