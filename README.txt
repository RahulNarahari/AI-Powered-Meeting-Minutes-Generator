1. audio_handler.py
What it does:
Converts audio files (like MP3, M4A, or others) to a standard format: 16kHz mono WAV.

Why it matters:
Speech models like Whisper and diarization tools need audio in this format to work properly.

2. transcription.py
What it does:
Uses the Whisper model to turn the audio into text, breaking it into segments with timestamps.

Why it matters:
You get a full written version of your meeting, with info about when things were said.

3. diarization.py
What it does:
Uses pyannote.audio to figure out when each person is speaking in the audio.

Why it matters:
Instead of one long block of text, you’ll know who said what — useful for interviews or group meetings.

⚠️ Needs a Hugging Face API token to work.

4. merger.py
What it does:
Matches the transcribed segments with speaker labels from diarization.

Why it matters:
Produces a clean transcript that looks like:

Speaker 1: Let's get started.
Speaker 2: Sure, here's the update.

5. summarizer.py
What it does:
Uses a BART model (a type of AI) to summarize the transcript into the main points.

Why it matters:
Helps you quickly understand what was discussed without reading the full transcript.

6. keywords.py
What it does:
Uses KeyBERT to find important terms or phrases that represent the key topics.

Why it matters:
Useful for tagging, indexing, or quickly seeing what the meeting was about.

7. sentiment.py
What it does:
Uses TextBlob to analyze the emotional tone (positive, negative, neutral) of the transcript.

Why it matters:
Helpful for gauging mood — e.g., a happy customer call vs. a complaint.

8. exporter.py
What it does:
Combines everything — transcript, speakers, summary, keywords, sentiment — and creates a PDF report.

Why it matters:
Gives you a neat, ready-to-share document of your meeting.

🧭 Use Case Example: Weekly Team Meeting
Record your team’s meeting.

Drop the audio file into the project folder.

Run the scripts one by one as per the instructions.

Get a full PDF report with:

What was said

Who said it

Summary of discussion

Key topics

Overall sentiment

