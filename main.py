import streamlit as st

# ऐप का टाइटल
st.title("किसान साथी")

# स्वागत संदेश बोलने के लिए JavaScript का उपयोग
welcome_text = "नमस्ते! किसान साथी ऐप में आपका स्वागत है। मैं आपकी खेती से जुड़ी जानकारी में मदद कर सकता हूँ।"
js_code = f"""
<script>
    var msg = new SpeechSynthesisUtterance("{welcome_text}");
    msg.lang = 'hi-IN';
    window.speechSynthesis.speak(msg);
</script>
"""
st.components.v1.html(js_code)

# आपका बाकी का ऐप कोड यहाँ लिखें
st.write("यहाँ अपनी खेती की जानकारी ढूँढें।")

