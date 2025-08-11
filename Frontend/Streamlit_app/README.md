# Streamlit Chat App (Production)

A simple Streamlit chat UI that connects to the FastAPI backend and streams replies in real-time. This app is intended for actual use (not testing) and keeps conversation context via `conversation_id`.

## Features
- Minimal chat interface using `st.chat_input`
- Real-time streaming of assistant responses
- Conversation persistence using backend-provided `conversation_id`
- Sidebar to configure backend URL at runtime

## Prerequisites
- Python 3.8+
- Backend API running (FastAPI) with the following endpoint:
  - `POST /chat-message` with params: `message`, `user_id`, `message_id`, `message_count`, optional `conversation_id`

## Install dependencies
From the project root:
```bash
pip install -r requirements.txt
```

## Start the backend
From the project root:
```bash
cd Backend/API_Program
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Run the Streamlit app
From the project root:
```bash
cd Frontend/Streamlit_app
streamlit run app.py
```
The app will open in your browser (default `http://localhost:8501`).

## Configuration
You can configure the backend URL in two ways:
- In-app sidebar, field "Backend URL"
- Environment variable before launching Streamlit:
  ```bash
  export API_BASE_URL="http://localhost:8000"
  ```

Optional environment variables:
- `DEFAULT_USER_ID` (default: `1`)

## Usage
1. Open the app and verify the backend URL in the sidebar.
2. Type a message in the chat input.
3. The app posts to the backend, streams the assistant's reply, and preserves `conversation_id` for context.

## Notes
- If the backend returns an error, the app will display it in the chat.
- `conversation_id` appears in the sidebar once assigned by the backend.
- This app intentionally avoids testing dashboards and DB tools; see `Frontend/Streamlit-Test` for the comprehensive test suite.

## File structure
```
Frontend/Streamlit_app/
├── app.py      # Streamlit chat application
└── README.md   # This file
```
