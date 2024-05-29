from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the chat model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Set page title and favicon
favicon_path = "./favicon.ico"  # Assuming favicon.ico is in the same directory
st.set_page_config(page_title="CHATBOT.ai", page_icon=favicon_path)

# Streamlit app title
st.markdown("<h1 style='text-align: center;'>AI CHATBOT</h1>", unsafe_allow_html=True)

# Version number
st.markdown("<h3 style='text-align: center; font-size: 12px;'>v1.0.1</h3>", unsafe_allow_html=True)

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Bold input label
st.markdown("**Input:**")
input = st.text_input("", key="input")  # Empty label since we are using markdown for label
submit = st.button("Ask the question")

# Add note below the input box
st.markdown("This site uses Gemini 1.0")

# Handle user input and get response
if submit and input:
    response = get_gemini_response(input)
    
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Add your picture and description
st.markdown("<hr>", unsafe_allow_html=True)
st.image("dmm.jpg", width=200, caption="DIVYANSH MITTAL (developer of CHATBOT.ai)", use_column_width=True)
st.markdown(
    """
    <div style='text-align: center;'>
        <h2>About Me: Divyansh Mittal, Creator of Chatbot.ai</h2>
        <p>Hey there! I'm Divyansh Mittal, the brain behind Chatbot.ai. At just 13 years old, I'm passionate about artificial intelligence and programming. Chatbot.ai is my brainchild, born out of my fascination with how technology can shape our future.</p>
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
