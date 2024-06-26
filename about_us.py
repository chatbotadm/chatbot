import os
import streamlit as st
def app():
    st.markdown("<h1 style='text-align: center;'>About</h1>", unsafe_allow_html=True)
    
    if os.path.exists("dmm.jpg"):
        st.image("dmm.jpg", width=200, caption="DIVYANSH MITTAL (Creator of CHATBOT.ai)", use_column_width=True)
    else:
        st.error("Developer image not found.")

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
