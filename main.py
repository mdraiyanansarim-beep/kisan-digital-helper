import streamlit as st

st.title("किसान साथी")

def speak_ai(text):
    js_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance("{text}");
    msg.lang = 'hi-IN';
    window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js_code, height=0)

message = "मैं आपका डिजिटल सहायक हूँ। मैं आपकी खेती से जुड़ी जानकारी में मदद कर सकता हूँ।"
speak_ai(message)

st.write(message)

user_input = st.text_input("अपनी समस्या यहाँ लिखें:")

if user_input:
    st.write(f"आपकी समस्या: {user_input} पर मैं काम कर रहा हूँ।")
