import streamlit as st
def app():
    st.header("Get in touch")
contact_form = """
<form action="https://formsubmit.co/chatbot.aidm@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Name" required>
     <textarea name="message" placeholder="Details of your problem"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)