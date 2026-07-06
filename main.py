import streamlit as st

st.title("किसान साथी")

# स्वागत संदेश
welcome_text = "नमस्ते! मैं आपका डिजिटल सहायक हूँ। मैं आपकी खेती से जुड़ी जानकारी में मदद कर सकता हूँ।"

# बटन ताकि यूजर क्लिक करके आवाज़ सुन सके
if st.button("आवाज़ सुनने के लिए यहाँ दबाएं"):
    js_code = f"""
    <script>
        var msg = new SpeechSynthesisUtterance("{welcome_text}");
        msg.lang = 'hi-IN';
        window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js_code, height=0)

st.write("अपनी खेती की जानकारी के लिए यहाँ पूछें।")



