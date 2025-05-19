from transformers import pipeline

def generate_summary(text, max_len=60):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_len, min_length=20, do_sample=False)
    return summary[0]['summary_text']
