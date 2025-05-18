from pyannote.audio import Pipeline

def diarize_speakers(audio_path, hf_token):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization",
                                        use_auth_token=hf_token)
    diarization = pipeline(audio_path)
    segments = []

    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append({
            "speaker": speaker,
            "start": turn.start,
            "end": turn.end
        })
    return segments