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
# Streamlit app title
st.markdown("<h1 style='text-align: center;'>AI CHATBOT</h1>", unsafe_allow_html=True)


# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Bold input label
st.markdown("**Input:**")
input = st.text_input("", key="input")  # Empty label since we are using markdown for label
submit = st.button("Ask the question")

# Add note below the input box
st.markdown("(This site uses Gemini 1.0)")

# Handle user input and get response
if submit and input:
    response = get_gemini_response(input)
    
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Add an image to the webpage
image_path = "./dmm.jpg"  # Assuming dmm.jpg is in the same directory
st.image(image_path, caption="Divyansh Mittal is a 13-year-old prodigy and the creative mind behind Chatbot.ai. With a passion for artificial intelligence and programming, Divyansh has embarked on a journey to revolutionize the way we interact with technology. Chatbot.ai is the culmination of his dedication and innovative spirit, offering users a glimpse into the future of AI-powered conversations.
Driven by curiosity and fueled by determination, Divyansh continues to push the boundaries of what's possible in the world of technology. With Chatbot.ai, he aims to make AI accessible and engaging for everyone, inspiring the next generation of creators and thinkers.", use_column_width=True)

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
