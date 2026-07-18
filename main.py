import streamlit as st
import google.generativeai as genai
from gtts import gTTS

st.set_page_config(page_title="किसान साथी AI", layout="centered")
st.title("🌾 किसान साथी AI")

# अपनी API Key यहाँ डालें (अगर नहीं है तो Google AI Studio से फ्री में ले लें)
api_key = "YOUR_API_KEY_HERE" 
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

query = st.text_input("अपनी समस्या यहाँ लिखें:")

if st.button("उत्तर खोजें"):
    if query:
        # AI से जवाब लें
        response = model.generate_content(f"आप एक कृषि विशेषज्ञ हैं। किसान के इस सवाल का जवाब दें: {query}")
        response_text = response.text
        st.write(response_text)

        # आवाज जनरेट करें
        tts = gTTS(text=response_text, lang='hi')
        tts.save("response.mp3")
        
        # ऑडियो प्ले करें
        audio_file = open("response.mp3", "rb")
        st.audio(audio_file.read(), format='audio/mp3')
    else:
        st.warning("कृपया अपनी समस्या लिखें।")
