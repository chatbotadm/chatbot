import streamlit as st
import base64
import os

def app():
    st.title("My Journey as a 13-Year-Old Developer")
    
    # Load and encode the image
    image_path = "blog.jpeg"
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        
        # Use inline CSS to resize the image
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{encoded_image}" style="width: 300px;">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error(f"Image not found at path: {image_path}")
    
    blog_content = """
    ### Introduction
    Hello everyone !, I  am Divyansh, a 13-year-old boy.I want to share, how I developed Chatbot.ai, a project that combines my love for coding and my interest in artificial intelligence.

    ### Getting Started
    My journey into the world of programming began when I was 10. I started with basic HTML and CSS, creating simple websites. Over the time, my curiosity grew, and I began learning more languages like JavaScript and Python. I was fascinated by how these languages could be used to create interactive and intelligent applications.

    ### The Idea Behind Chatbot.ai
    The inspiration for Chatbot.ai came from my desire to make technology more accessible and interactive. I wanted to build something that could understand and respond to users in a meaningful way. The idea was to create a chatbot that could help people with various tasks, from answering questions to providing recommendations.

    ### Development Process
    Creating Chatbot.ai involved several steps:

    - **Learning AI and Machine Learning**: I started by learning the basics of artificial intelligence and machine learning. Online resources like Coursera and Harvard were incredibly helpful.
    
    - **Designing the Bot**: I planned the chatbot's functionalities and user interface. I wanted it to be user-friendly and capable of understanding natural language.
    
    - **Coding**: Using Python and libraries like TensorFlow, I began coding the chatbot. I implemented natural language processing (NLP) to enable the bot to understand and respond to user queries.
    
    - **Testing and Improving**: After building the initial version, I tested it extensively. I gathered feedback from friends and family, which helped me identify areas for improvement.

    ### Challenges Faced
    One of the biggest challenge, I faced was ensuring that the chatbot could understand and respond accurately to a wide range of queries. This required a lot of fine-tuning and training the model with diverse datasets. Another challenge was optimizing the chatbot's performance to ensure it could handle multiple users simultaneously.

    ### Launching Chatbot.ai
    After months of hard work, Chatbot.ai was finally ready for launch. I created a simple website where users could interact with the bot. The response has been overwhelmingly positive, and it's exciting to see people using something I created.

    ### Future Plans
    I have plans for Chatbot.ai. I want to add more features, like voice recognition and integration with other services. I'm also exploring ways to make the chatbot more intuitive and personalized.

    ### Conclusion
    My journey as a young developer has been incredibly rewarding. Creating Chatbot.ai has taught me so much about coding, problem-solving, and the power of perseverance. If you're a young aspiring developer, my advice is to never stop learning and experimenting. The possibilities are endless, and with determination and consistent approach, you can achieve anything.

    Thank you for reading! If you have any questions or feedback, please contact me at <a href="mailto:chatbot.aidm@gmail.com">chatbot.aidm@gmail.com</a>.
    """
    st.markdown(blog_content, unsafe_allow_html=True)
