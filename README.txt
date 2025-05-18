AI-Powered Meeting Minutes Generator
------------------------------------

Modules:
- audio_handler.py: Converts audio files to WAV format
- transcription.py: Transcribes speech to text using Whisper
- diarization.py: Performs speaker diarization with pyannote.audio
- merger.py: Combines transcript with speaker labels
- summarizer.py: Summarizes text using BART
- keywords.py: Extracts keywords using KeyBERT
- sentiment.py: Analyzes sentiment with TextBlob
- exporter.py: Generates a PDF report

Instructions:
1. Place your meeting audio file (e.g., .mp3, .wav) in the project directory.
2. Run convert_to_wav() to convert to 16kHz mono WAV.
3. Use transcribe_audio() to get transcript and segments.
4. Use diarize_speakers() with your Hugging Face token.
5. Merge speaker labels using merge_transcript().
6. Run summarize_text() to get the meeting summary.
7. Extract keywords using extract_keywords().
8. Analyze sentiment with analyze_sentiment().
9. Generate your report using export_to_pdf().