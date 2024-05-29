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

# Bold input label
st.markdown("**Input:**")
input = st.text_input("", key="input")  # Empty label since we are using markdown for label
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
        <p><a href="mailto:support@example.com">support@example.com</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

