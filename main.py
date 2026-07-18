import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="किसान साथी AI", layout="centered")
st.title("🌾 किसान साथी AI")

query = st.text_input("अपनी समस्या यहाँ लिखें:")

if st.button("उत्तर खोजें"):
    if query:
        # यहाँ हम AI का जवाब सेट करेंगे
        response_text = "फसल सुरक्षा के लिए आप नीम के अर्क का उपयोग कर सकते हैं। यह कीड़ों को दूर रखने का प्राकृतिक तरीका है।"
        st.write(response_text)

        # आवाज जनरेट करें
        tts = gTTS(text=response_text, lang='hi')
        tts.save("response.mp3")
        
        # ऑडियो प्ले करें
        audio_file = open("response.mp3", "rb")
        st.audio(audio_file.read(), format='audio/mp3')
    else:
        st.warning("कृपया अपनी समस्या लिखें।")




