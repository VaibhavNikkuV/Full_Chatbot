import mysql.connector
import os
import sys
import random
import string
from datetime import datetime
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import json

load_dotenv()

sys.path.insert(1, "/Users/vaibhavarya187/Personal/Personal/VibeCoding/Chatbot/Main")
from Chatbot import main as chatbot_main


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_SSL_CA = os.getenv("DB_SSL_CA")

# Database Connection
def db_connection():
    db = mysql.connector.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        ssl_ca=DB_SSL_CA
    )
    return db


app = FastAPI()


# Generate random varchar(16) ID
def generate_random_id():
    chars = string.ascii_lowercase + string.digits
    parts = [8, 4]
    result = '-'.join(''.join(random.choices(chars, k=p)) for p in parts)
    return result



# Root API
@app.get("/")
def root():
    return {"status": "Working"}



# Health Check API
@app.get("/health")
def health():
    return {"status": "Healthy"}



# Chat Message API
@app.post("/chat-message")
def chat_message(message: str, user_id: int, message_id: str, message_count: int, conversation_id: str = ""):
    try:
        # print(f"Received: message={message}, user_id={user_id}, message_count={message_count}")


        # Reset message count for new conversations
        print("Okay 1")
        if message_count == 1:
            message_count = 0

        print("message: ", message)
        print("conversation_id: ", conversation_id)

        # Get chatbot response
        print("Okay 1.1")
        response = chatbot_main(message, conversation_id)

        print("Response: ", response)


        if not response:
            raise HTTPException(status_code=500, detail="Empty response from chatbot_main")

        try:
            responseFormatted = json.loads(response)
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Invalid JSON returned by chatbot_main")


        print("Type of response: ", type(response))
        print("Okay 1.2")

        responseFormatted = json.loads(response)
        conversation_id = responseFormatted.get("conversation_id")
        print("Okay 1.3")
        # Generate unique message IDs for user and assistant messages
        user_message_id = generate_random_id() if message_id == "" else message_id
        assistant_message_id = generate_random_id()
        print("Okay 1.5")
        # Connect to database
        db = db_connection()
        cursor = db.cursor()
        print("Okay 2")

        # Insert the user message into message_store table
        user_query = """INSERT INTO message_store 
                       (role, conv_id, message_no, message_id, message, elapsed_time, Status, created_at, updated_at) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(user_query, ("user", conversation_id, message_count, user_message_id, message, 0, "Success", datetime.now(), datetime.now()))
        db.commit()  # COMMIT THE USER MESSAGE
        db.close()
        print("Okay 3")
        db = db_connection()
        cursor = db.cursor()
        print("Okay 4")
        assistant_message = responseFormatted.get("message")
        # Insert the assistant message into message_store table
        assistant_query = """INSERT INTO message_store 
                            (role, conv_id, message_no, message_id, message, elapsed_time, Status, created_at, updated_at) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(assistant_query, ("assistant", conversation_id, message_count + 1, assistant_message_id, assistant_message, 0, "Success", datetime.now(), datetime.now()))
        db.commit()  # COMMIT THE ASSISTANT MESSAGE
        db.close()  # CLOSE THE CONNECTION
        print("Okay 5")
        # Create conversation record only for new conversations (message_count == 0)
        # Note: ID field is auto_increment, so we don't include it
        if message_count == 0:
            db = db_connection()
            cursor = db.cursor()
            conversation_query = """INSERT INTO conversation_store 
                                   (chat_name, conv_id, user_id, message_count, created_at, updated_at) 
                                   VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(conversation_query, ("NEW CHAT", conversation_id, user_id, 2, datetime.now(), datetime.now()))  # 2 messages: user + assistant
            db.commit()  # COMMIT THE CONVERSATION
            db.close()
        print("Okay 6")
        return {"message": assistant_message, "conversation_id": conversation_id}
        
    except Exception as e:
        # print("Here 1")
        raise HTTPException(status_code=500, detail=str(e))




# Get Conversation History API
@app.get("/get-conversation-history/{conversation_id}")
def get_conversation_history(conversation_id: str):
    """Get conversation history for a specific conversation ID."""
    try:
        db = db_connection()
        cursor = db.cursor()
        
        # Get messages ordered by message_no
        query = """
        SELECT 
            ID, role, message_no,
            message
        FROM message_store
        WHERE conv_id = %s
        ORDER BY ID ASC;
        """
        cursor.execute(query, (conversation_id,))
        messages = cursor.fetchall()

        db.close()

        # return {
        #     "messages": messages
        # }
        
        # Convert to structured format
        conversation_history = []
        for message in messages:
            conversation_history.append({
                "role": message[1],
                "message": message[3]   
            })
        
        return {
            "conversation_id": conversation_id,
            "message_count": len(conversation_history),
            "messages": conversation_history
        }
        
    except Exception as e:
        # print("Here 2")
        raise HTTPException(status_code=500, detail=str(e))


