import streamlit as st
from PIL import Image
import numpy as np
from fer import FER

# Page title
st.set_page_config(page_title="AI Mirror - Emotion Detector", layout="centered")
st.title("🪞 AI Mirror")
st.markdown("Upload your image and let AI detect your emotion!")

# Emoji Map
emoji_map = {
    "angry": "😠",
    "disgust": "🤢",
    "fear": "😨",
    "happy": "😄",
    "sad": "😢",
    "surprise": "😲",
    "neutral": "😐"
}

# File Uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("Analyzing emotion...")

    # Load and preprocess image
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    # Emotion Detection
    detector = FER()
    result = detector.top_emotion(image_np)

    if result:
        emotion, score = result
        emoji = emoji_map.get(emotion, "")
        st.subheader(f"Detected Emotion: **{emotion.capitalize()}** {emoji}")
        st.write(f"Confidence Score: `{score * 100:.2f}%`")
    else:
        st.warning("Couldn't detect a face or emotion. Try a different image.")
