# AI-Powered Video Summary Generator

A powerful Streamlit web app that allows users to upload MP4 video files, automatically transcribes the audio using OpenAI Whisper, summarizes key points using HuggingFace Transformers, and extracts actionable insights.

---

## Features

- **Audio Transcription** – Converts speech to text using Whisper
- **Text Summarization** – Condenses transcripts with BART (HuggingFace)
- **Action Item Extraction** – Highlights tasks and key decisions
- **NLP + Video Processing** – Combines cutting-edge AI tools
- **Planned**: Timeline summaries, speaker identification, TTS playback

---

## Tech Stack

- **Python 3.12**
- [Streamlit](https://streamlit.io/) – Web UI
- [OpenAI Whisper](https://github.com/openai/whisper) – Speech recognition
- [Transformers](https://huggingface.co/docs/transformers) – NLP models
- `moviepy`, `pydub`, `ffmpeg-python` – Video/audio support

---

## Project Structure

```
VideoSummaryGenerator/
│
├── app.py              # Streamlit frontend
├── utils.py            # NLP/audio functions
├── requirements.txt    # Dependencies
└── uploads/            # Uploaded video storage
```

---

## Installation

```bash
git clone https://github.com/your-username/video-summary-generator.git
cd video-summary-generator
pip install -r requirements.txt
```

---

## Run the App

```bash
streamlit run app.py
```

Then open your browser and go to:  
`http://localhost:8505`

---

## Sample Output

- **Transcript:** Full speech converted to text  
- **Summary:** Condensed version of what was said  
- **Action Items:** "Must", "should", "need to", and similar tasks extracted

---

## Future Enhancements

- Speaker Identification  
- Multi-language Support  
- Text-to-Speech Summary  
- Timeline-based summary viewer
