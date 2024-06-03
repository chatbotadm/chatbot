import streamlit as st

def app():
    st.title("What's New ?")
    st.markdown(
        """
        ## Version 1.0.2 beta (Updated on June 3,2024) 
        - Added Stable Diffusion image generation.
        - Initial release with core functionalities.
        - Integrated Gemini 1.5 for better chat responses.
        - Enhanced UI for better user experience.
        
        ## Version 1.0.1 (Updated on May 31,2024) 
        - Bug fixes and performance improvements.

        ## Version 1.0.0 (Released on May 29,2024) 
        - Initial release of Chatbot.ai
        
        ## Upcoming Features - 
        - Live speech-to-text transcription
        - Additional customization options for generated images.
        - Ability to read PDF,video to give a summary
        - More robust error handling 
        - Security patches
        """
    )
