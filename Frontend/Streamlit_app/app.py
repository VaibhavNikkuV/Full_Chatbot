import os
import time
import json
import string
import random
import requests
import streamlit as st


def generate_random_id() -> str:
    chars = string.ascii_lowercase + string.digits
    parts = [8, 4]
    return '-'.join(''.join(random.choices(chars, k=p)) for p in parts)


def stream_text(text: str):
    for ch in text:
        yield ch
        time.sleep(0.008)


# Basic page config
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")


# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []  # [{role: "user"|"assistant", content: str}]

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None

if "api_base_url" not in st.session_state:
    st.session_state.api_base_url = os.getenv("API_BASE_URL", "http://localhost:8000")

if "user_id" not in st.session_state:
    # Keep simple: single local user; can be overridden via env DEFAULT_USER_ID
    st.session_state.user_id = int(os.getenv("DEFAULT_USER_ID", "1"))


st.title("🤖 Chatbot")
st.caption("Type a message and get responses powered by the backend API")


with st.sidebar:
    st.subheader("Settings")
    st.session_state.api_base_url = st.text_input(
        "Backend URL",
        value=st.session_state.api_base_url,
        help="FastAPI base URL",
    )
    st.write("")
    st.text(f"Conversation: {st.session_state.conversation_id or '-'}")


# Render history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
user_input = st.chat_input("Your message...")

if user_input:
    # Echo user message immediately
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Prepare backend call
    api_base_url = st.session_state.api_base_url.rstrip("/")
    message_id = generate_random_id()
    message_count = len([m for m in st.session_state.messages if m["role"] == "user"])  # aligns with backend expectation
    conversation_id = st.session_state.conversation_id or ""

    # Call backend and render assistant message
    with st.chat_message("assistant"):
        placeholder = st.empty()
        try:
            resp = requests.post(
                f"{api_base_url}/chat-message",
                params={
                    "message": user_input,
                    "user_id": st.session_state.user_id,
                    "message_id": message_id,
                    "message_count": message_count,
                    "conversation_id": conversation_id,
                },
                timeout=60,
            )

            if resp.status_code != 200:
                error_text = f"API Error: {resp.status_code} - {resp.text}"
                placeholder.error(error_text)
                st.session_state.messages.append({"role": "assistant", "content": error_text})
            else:
                data = resp.json()
                bot_message = data.get("message", "")
                st.session_state.conversation_id = data.get("conversation_id") or st.session_state.conversation_id

                # Stream the response for a real-time feel
                placeholder.write_stream(stream_text(bot_message))
                st.session_state.messages.append({"role": "assistant", "content": bot_message})

        except Exception as e:
            error_text = f"Connection Error: {str(e)}"
            placeholder.error(error_text)
            st.session_state.messages.append({"role": "assistant", "content": error_text})


