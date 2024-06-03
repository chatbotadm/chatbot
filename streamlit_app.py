import os
import base64
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import torch
from PIL import Image

# Import the "What's New?" page, Privacy Policy page, and Terms of Use page
import whats_new
import terms_of_use
import privacy_policy

# Set page title and favicon
favicon_path = "./favicon.ico"
if os.path.exists(favicon_path):
    st.set_page_config(page_title="CHATBOT.ai", page_icon=favicon_path)
else:
    st.set_page_config(page_title="CHATBOT.ai")

# Load custom CSS
def load_css(file_name):
    with open(file_name, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('styles.css')

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

# Lazy loading for Stable Diffusion model
@st.cache_resource
def load_model():
    from diffusers import StableDiffusionPipeline
    try:
        model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
        if torch.cuda.is_available():
            model = model.to("cuda")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Display the logo
logo_path = "final logo.png" 
if os.path.exists(logo_path):
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{base64.b64encode(open(logo_path, "rb").read()).decode()}">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning(f"Logo not found at path: {logo_path}")

# Sidebar navigation
st.sidebar.title("Welcome to Chatbot.ai")

def set_nav_item(nav_item):
    st.session_state.selected_nav_item = nav_item

if 'selected_nav_item' not in st.session_state:
    st.session_state.selected_nav_item = "Chatbot"

nav_items = {
    "Chatbot": "Chatbot",
    "What's New?": "What's New?",
    "Privacy Policy": "Privacy Policy",
    "Terms of Use": "Terms of Use"
}

for nav_item, display_name in nav_items.items():
    if st.sidebar.button(display_name, key=nav_item):
        set_nav_item(nav_item)

st.markdown(
    f"""
    <style>
        .sidebar .sidebar-content .nav-item {{
            padding: 10px 20px;
            color: white;
            cursor: pointer;
            transition: all 0.3s;
        }}
        .sidebar .sidebar-content .nav-item:hover,
        .sidebar .sidebar-content .nav-item.selected {{
            background-color: #444;
            border-radius: 5px;
            color: white;
        }}
    </style>
    """, 
    unsafe_allow_html=True
)

page = st.session_state.selected_nav_item
if page == "Chatbot":
    st.markdown("<h1 style='text-align: center;'>AI CHATBOT</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-size: 12px;'>v1.0.2 beta</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 10px;'>Note: This is a beta version and may contain bugs.</p>", unsafe_allow_html=True)

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    st.markdown("**Input:**")
    user_input = st.text_input("", key="input")
    ask_question = st.button("Ask the question")
    generate_image = st.button("Generate Image")

    st.markdown("This site uses Gemini 1.5")

    if ask_question and user_input:
        try:
            response = get_gemini_response(user_input)
            st.session_state['chat_history'].append(("You", user_input))
            st.subheader("The Response is")
            for chunk in response:
                st.write(chunk.text)
                st.session_state['chat_history'].append(("Bot", chunk.text
