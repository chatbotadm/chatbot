from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure the API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the chat model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Set up SQLite database for logging
conn = sqlite3.connect('search_logs.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS search_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_query TEXT,
        bot_response TEXT,
        user_identifier TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

def log_search_query(user_query, bot_response, user_identifier):
    try:
        cursor.execute('''
            INSERT INTO search_logs (user_query, bot_response, user_identifier, timestamp) VALUES (?, ?, ?, ?)
        ''', (user_query, bot_response, user_identifier, datetime.now()))
        conn.commit()
        print("Log entry added successfully.")
    except Exception as e:
        print(f"Error logging search query: {e}")

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    full_response = ""
    for chunk in response:
        full_response += chunk.text
    return full_response

# Set page title and favicon
favicon_path = "./favicon.ico"  # Assuming favicon.ico is in the same directory
st.set_page_config(page_title="CHATBOT.ai", page_icon=favicon_path)

# Streamlit app title
st.markdown("<h1 style='text-align: center;'>AI CHATBOT</h1>", unsafe_allow_html=True)

# Version number
st.markdown("<h3 style='text-align: center; font-size: 12px;'>v1.0.1</h3>", unsafe_allow_html=True)

# Initialize chat history for all users
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = {}

# Get user identifier (using IP address for simplicity)
user_identifier = st.session_state.session._context['ip']

# Initialize chat history for this user if it doesn't exist
if user_identifier not in st.session_state['chat_history']:
    st.session_state['chat_history'][user_identifier] = []

# Bold input label
st.markdown("**Input:**")
input = st.text_input("User Query", label_visibility='hidden', key="input")  # Non-empty label hidden for accessibility
submit = st.button("Ask the question")

# Add note below the input box
st.markdown("This site uses Gemini 1.0")

# Handle user input and get response
if submit and input:
    response = get_gemini_response(input)
    
    st.session_state['chat_history'][user_identifier].append(("You", input))
    st.subheader("The Response is")
    st.write(response)
    st.session_state['chat_history'][user_identifier].append(("Bot", response))

    # Log the query and response
    log_search_query(input, response, user_identifier)

# Add your picture and description
st.markdown("<hr>", unsafe_allow_html=True)
st.image("dmm.jpg", width=200, caption="DIVYANSH MITTAL (developer of CHATBOT.ai)", use_column_width=True)
st.markdown(
    """
    <div style='text-align: center;'>
        <h2>About Me: Divyansh Mittal, Creator of Chatbot.ai</h2>
        <p>Hey there! I'm Divyansh Mittal, the brains behind Chatbot.ai. At just 13 years old, I'm passionate about artificial intelligence and programming. Chatbot.ai is my brainchild, born out of my fascination with how technology can shape our future.</p>
        <p>With Chatbot.ai, I'm on a mission to revolutionize the way we interact with AI. My goal is to make AI accessible and engaging for everyone, inspiring the next generation of creators and thinkers.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Add a black section for support email
st.markdown(
    """
    <style>
    .support-section {
        background-color: black;
        color: white;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
    }
    .support-section a {
        color: white;
        text-decoration: none;
    }
    .support-section a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="support-section">
        <h4>Support</h4>
        <p>If you have any questions or need support, please contact us at:</p>
        <p><a href="mailto:chatbot.aidm@gmail.com">chatbot.aidm@gmail.com</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
