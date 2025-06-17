import streamlit as st
import os
from utils import transcribe_audio, summarize_text, extract_action_items

# Page configuration
st.set_page_config(page_title="Video Summary Generator", layout="centered")
st.title("AI-Powered Video Summary Generator")

# Create uploads directory if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# File uploader
uploaded_file = st.file_uploader("Upload an MP4 video file", type=["mp4"])

if uploaded_file:
    file_path = os.path.join("uploads", uploaded_file.name)
    
    # Save uploaded video file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("✅ File uploaded successfully!")

    # Transcription
    with st.spinner("Transcribing audio..."):
        transcript = transcribe_audio(file_path)
        st.subheader("📄 Transcript")
        st.write(transcript)

    # Summarization
    with st.spinner("Generating summary..."):
        summary = summarize_text(transcript)
        st.subheader("📝 Summary")
        st.write(summary)

    # Action items
    with st.spinner("Extracting action items..."):
        actions = extract_action_items(transcript)
        st.subheader("✅ Action Items")
        if actions:
            for item in actions:
                st.markdown(f"- {item}")
        else:
            st.info("No clear action items detected.")