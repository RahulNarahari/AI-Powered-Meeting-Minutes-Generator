import openai

def transcribe_audio(audio_path):
    client = openai.OpenAI(api_key="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")  # Replace with your real key

    with open(audio_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=file
        )
    return transcription.text

