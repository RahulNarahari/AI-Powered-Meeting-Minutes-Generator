def merge_transcript(segments, speaker_data):
    output = []
    for seg in segments:
        start = seg['start']
        text = seg['text']
        speaker = "Unknown"
        for s in speaker_data:
            if s['start'] <= start <= s['end']:
                speaker = s['speaker']
                break
        output.append(f"{speaker}: {text}")
    return "\n".join(output)