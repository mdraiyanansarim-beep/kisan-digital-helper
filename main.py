import streamlit as st
import google.generativeai as genai
from gtts import gTTS

# API Key को Streamlit के Secrets से लें
api_key = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="किसान साथी AI", layout="centered")
st.title("🌾 किसान साथी AI")

query = st.text_input("अपनी समस्या यहाँ लिखें:")

if st.button("उत्तर खोजें"):
    if query:
        # AI का जवाब
        response = model.generate_content(f"आप एक कृषि विशेषज्ञ हैं। किसान के इस सवाल का जवाब दें: {query}")
        response_text = response.text
        st.write(response_text)

        # आवाज जनरेट करें
        tts = gTTS(text=response_text, lang='hi', slow=False)
        tts.save("response.mp3")
        
        # ऑडियो प्ले करें
        st.audio("response.mp3", format='audio/mp3')
    else:
        st.warning("कृपया अपनी समस्या लिखें।")
