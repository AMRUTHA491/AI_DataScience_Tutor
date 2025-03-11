
import uuid
import streamlit as st
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
import base64
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# Set up Streamlit Page
st.set_page_config(page_title="AI Data Science Tutor", layout="wide")

# Background Image Setup
local_image_path = r"C:\Users\user\Downloads\Datasets\Datasets\AI_DataScience_Tutor\white_background.jpg"

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

base64_image = get_base64_image(local_image_path)

# Custom CSS for chat layout
chat_styles = f"""
<style>
    .stApp {{
        background: url("data:image/jpeg;base64,{base64_image}") no-repeat center center fixed;
        background-size: cover;
        width: 70%; /* Reduce window width */
        max-width: 900px; /* Limit maximum width */
        margin: 20px auto; /* Center the window with some top margin */
        border-radius: 12px; /* Rounded corners for all sides */
        overflow: hidden; /* Prevent background overflow */
        padding: 20px;
    }}
    .chat-container {{
        background: transparent; /* No white bar */
        width: 100%; /* Full width */
        padding: 20px;
    }}
    .chat-message {{
        padding: 10px;
        margin: 8px 0;
        border-radius: 15px;
        display: inline-block;
        max-width: 70%;
        word-wrap: break-word;
    }}
    .user-message {{
        background-color: #dcf8c6;
        text-align: right;
        align-self: flex-end;
        float: right;
        clear: both;
    }}
    .ai-message {{
    background-color: #DFF6FF;
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
    align-self: flex-start;
    border-radius: 20px; /* Increased border-radius */
    max-width: 70%;
    word-wrap: break-word;
    display: inline-block;
}}
</style>
"""
st.markdown(chat_styles, unsafe_allow_html=True)

# Chat Header
st.markdown("<h2 style='text-align: center; color: black;'>🤖 ChatDS AI: Interactive Data Science Guide</h2>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: black;'>💬 Talk to your AI Data Science buddy and get spot-on answers to all your DS questions! 😎📊</h6>",
    unsafe_allow_html=True,
)

# Function to retrieve chat history from SQLite
def get_chat_message_history(session_id):
    return SQLChatMessageHistory(
        session_id=session_id,
        connection="sqlite:///C:/Users/user/Downloads/Datasets/Datasets/AI_DataScience_Tutor/SQL_database/sqlite.db",
    )

# Chat prompt template
chat_template = ChatPromptTemplate(
    messages=[
        ("system", "You are an AI Data Science Tutor. If the query is unrelated to data science, politely redirect.The information should be simple and easily understandable."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{user_input}"),
    ]
)

# AI Model
model = ChatGoogleGenerativeAI(api_key=api_key, model="gemini-1.5-pro")
output_parser = StrOutputParser()
chain = chat_template | model | output_parser

# Conversation Chain with Memory
conversation_chain = RunnableWithMessageHistory(
    chain, 
    get_chat_message_history, 
    input_messages_key="user_input", 
    history_messages_key="chat_history"
)

# Initialize Session State
if "session_id" not in st.session_state:
    st.session_state.session_id = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# Ask user for session restoration

choice = st.radio("Do you have a previous session?", ["Yes", "No"])


if choice == "Yes":
    user_id = st.text_input("Enter your Session ID:")
    if user_id:
        st.session_state.session_id = user_id
        st.success(f"✅ Restored session: {user_id}")
elif choice == "No":
    user_id = str(uuid.uuid4())  # Generate new session
    st.session_state.session_id = user_id
    st.success(f"New session started! Your Session ID: {user_id}")

# Function to interact with AI model
def chat_bot(session_id, prompt):
    config = {"configurable": {"session_id": session_id}}
    input_prompt = {"user_input": prompt}
    response_stream=conversation_chain.stream(input_prompt, config=config)

    full_response = ""
    response_container = st.empty()
    with response_container:
        response_box = st.empty()  # White box for streaming text

        for chunk in response_stream:
            full_response += chunk  # Append each chunk
            response_box.markdown(f"<div class='ai-message'>{full_response}</div>", unsafe_allow_html=True)

    return full_response



# Display chat messages
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for message in st.session_state.messages:
    role_class = "user-message" if message["role"] == "user" else "ai-message"
    st.markdown(f'<div class="chat-message {role_class}">{message["content"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# User Input
user_input = st.chat_input("Type your message...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f'<div class="chat-message user-message">{user_input}</div>', unsafe_allow_html=True)

    # Get AI Response
    response = chat_bot(st.session_state.session_id, user_input)

    # Store AI message
    st.session_state.messages.append({"role": "assistant", "content": response})
    

