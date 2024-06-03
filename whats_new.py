import streamlit as st

def app():
    st.title("What's New ?")
    st.markdown(
        """
        ## Version 1.0.2 beta
        - Added Stable Diffusion image generation.
        - Initial release with core functionalities.
        - Integrated with Gemini AI for chat responses.
        - Enhanced UI for better user experience.
        
        ## Version 1.0.1 
        - Bug fixes and performance improvements.
        
        ## Upcoming Features
        - Live speech-to-text transcription
        - Additional customization options for generated images.
        - Ability to read PDF,video to give a summary
        - More robust error handling 
        - Security patches
        """
    )
