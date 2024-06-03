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
        model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", low_cpu_mem_usage=True)
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

    st.markdown("<p style='font-size: 10px; text-align: center;'>Image generation can take up to 15 mins depending on your system.</p>", unsafe_allow_html=True)
    st.markdown("This site uses Gemini 1.5")
    

    if ask_question and user_input:
        try:
            response = get_gemini_response(user_input)
            st.session_state['chat_history'].append(("You", user_input))
            st.subheader("The Response is")
            for chunk in response:
                st.write(chunk.text)
                st.session_state['chat_history'].append(("Bot", chunk.text))
        except Exception as e:
            st.error(f"Error getting chatbot response: {e}")

    if generate_image and user_input:
        sd_model = load_model()
        if sd_model:
            progress_bar = st.progress(0)
            with st.spinner("Generating Image..."):
                try:
                    with torch.no_grad():
                        image = sd_model(user_input).images[0]
                    progress_bar.progress(50)
                    st.image(image, caption="Here is your image", use_column_width=True)
                    progress_bar.progress(100)
                except Exception as e:
                    st.error(f"Error generating image: {e}")
        else:
            st.error("Stable Diffusion model not loaded.")

    st.markdown("<hr>", unsafe_allow_html=True)
    if os.path.exists("dmm.jpg"):
        st.image("dmm.jpg", width=200, caption="DIVYANSH MITTAL (Creator of Chatbot.AI)", use_column_width=True)
    else:
        st.error("Developer image not found.")

    st.markdown(
        """
        <div style='text-align: center;'>
            <h2>About Me: Divyansh Mittal, Creator of Chatbot.AI</h2>
            <p>Hey there! I'm Divyansh Mittal, the brain behind Chatbot.ai. At just 13 years old, I'm passionate about artificial intelligence and programming. Chatbot.ai is my brainchild, born out of my fascination with how technology can shape our future.</p>
            <p>With Chatbot.ai, I'm on a mission to revolutionize the way we interact with AI. My goal is to make AI accessible and engaging for everyone, inspiring the next generation of creators and thinkers.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

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

elif page == "What's New?":
    whats_new.app()

elif page == "Privacy Policy":
    privacy_policy.app()

elif page == "Terms of Use":
    terms_of_use.app()
