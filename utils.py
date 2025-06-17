import whisper
from transformers import pipeline

def transcribe_audio(file_path):
    model = whisper.load_model("base")  # You can change to "small", "medium", or "large"
    result = model.transcribe(file_path)
    return result['text']

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    # Break text into smaller chunks (1000 characters each)
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""
    for chunk in chunks:
        summary += summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    return summary

def extract_action_items(text):
    lines = text.split('.')
    keywords = ['should', 'need to', 'must', 'recommended']
    actions = [line.strip() for line in lines if any(word in line.lower() for word in keywords)]
    return actions