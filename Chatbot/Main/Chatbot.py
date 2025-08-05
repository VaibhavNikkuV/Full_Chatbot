# Chatbot.py

import mysql.connector
import os
import sys
import json
from openai import OpenAI
import string
import random
from dotenv import load_dotenv

load_dotenv()

# Environment Variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_SSL_CA = os.getenv("DB_SSL_CA")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Database Connection
def db_connection():
    return mysql.connector.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        ssl_ca=DB_SSL_CA
    )

# Generate Conversation ID
def generate_random_id():
    chars = string.ascii_lowercase + string.digits
    parts = [8, 4]
    return '-'.join(''.join(random.choices(chars, k=p)) for p in parts)

# OpenAI Chatbot Class
class OpenAIChatbot:
    def __init__(self):
        api_key = OPENAI_API_KEY
        if not api_key:
            print("Error: OPENAI_API_KEY not found in environment variables.")
            sys.exit(1)
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"

    def get_response(self, user_message: str, conversation_id: str):
        try:
            history_str = ""

            # Fetch previous messages if conversation ID exists
            if conversation_id:
                db = db_connection()
                cursor = db.cursor()
                query = f"SELECT role, message FROM message_store WHERE conv_id = '{conversation_id}' ORDER BY ID ASC;"
                cursor.execute(query)
                result = cursor.fetchall()
                db.close()

                conversation_messages = []
                for row in result:
                    conversation_messages.append({"role": row[0], "message": row[1]})

                print("Conversation Messages type: ", type(conversation_messages))

                for i in conversation_messages:
                    history_str += f"{i['role']}: {i['message']}\n"
            else:
                history_str = "It's a new conversation."

            # Always generate a new conversation ID (if none given)
            if not conversation_id:
                conversation_id = generate_random_id()

            messages = [
                {"role": "system", "content": "You are a helpful assistant. Be concise and friendly."},
                {"role": "user", "content": f"The conversation history is as follows: {history_str}\nUser: {user_message}"}
            ]

            # OpenAI API call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=512,
                temperature=0.7
            )

            formatted_response = {
                "message": response.choices[0].message.content,
                "conversation_id": conversation_id
            }

            return json.dumps(formatted_response)

        except Exception as e:
            return json.dumps({"error": str(e)})

    def chat(self, query: str, conversation_id: str):
        if not query or not query.strip():
            return json.dumps({"error": "No message provided"})

        response = self.get_response(query, conversation_id)

        # Prevent JSON decoding errors
        try:
            response = json.loads(response)
        except json.JSONDecodeError:
            return json.dumps({"error": "Invalid response from OpenAI"})

        if "error" in response:
            return json.dumps(response)

        return json.dumps({
            "message": response["message"],
            "conversation_id": response["conversation_id"]
        })

# Main Function
def main(query: str, conversation_id: str):
    if not query:
        return json.dumps({"error": "No query provided"})

    chatbot = OpenAIChatbot()
    response = chatbot.chat(query, conversation_id)

    # Final safeguard in case of errors
    try:
        response = json.loads(response)
        print("Response: ", response)
    except json.JSONDecodeError:
        return json.dumps({"error": "Failed to parse response"})

    return json.dumps(response)

if __name__ == "__main__":
    query = "Hello"
    conversation_id = ""
    print(main(query, conversation_id))
