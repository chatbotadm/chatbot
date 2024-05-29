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
st.header("AI CHATBOT")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input field
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# Handle user input and get response
if submit and input:
    response = get_gemini_response(input)
    
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display chat history
st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")

# Add an image to the webpage
image_path = "./dmm.jpg"  # Assuming dmm.jpg is in the same directory
st.image(image_path, caption="DIVYANSH MITTAL (developer of CHATBOTst.ai)", use_column_width=True)
