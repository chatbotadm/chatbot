from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app)
    python3 __init__.py
    st.markdown("<p style='text-align: center; font-size: 10px;'>Note: This is a beta version and may contain bugs.</p>", unsafe_allow_html=True)
