import streamlit as st

def app():
    st.title("What's New ?")
    st.markdown(
        """
        ## Version 1.0.3 beta (Updated on June 7,2024)
        - Added icons in sidebar menu.
        - Fixed bugs 
        
        ## Version 1.0.2 (Updated on June 3,2024)
        - Added Stable Diffusion image generation.
        - Initial release with core functionalities.
        - Integrated with Gemini AI for chat responses.
        - Enhanced UI for better user experience.
        
        ## Version 1.0.1 (Updated on May 31,2024)
        - Bug fixes and performance improvements.
        
        ## Version 1.0.0 (Updated on May 30,2024)
        - Initial release of Chatbot.ai
        
        ## Upcoming Features
        - Live speech-to-text transcription
        - UI Enhancements
        - Additional customization options for generated images.
        - Ability to read PDF,video to give a summary
        - More robust error handling 
        - Security patches
        
        """
    )
