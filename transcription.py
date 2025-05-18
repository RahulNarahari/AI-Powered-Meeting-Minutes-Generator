import whisper

def transcribe_audio(file_path, model_size="base"):
    model = whisper.load_model(model_size)
    print("Transcribing...")
    result = model.transcribe(file_path)
    return result['text'], result['segments']