import streamlit as st
from transcribe import transcribe_audio
from clean import clean_text
from summarizer import generate_summary
from extract import extract_action_items

st.set_page_config(page_title="AI Meeting Minutes Generator", layout="centered")
st.title("🧠 AI-Powered Meeting Minutes Generator")

uploaded = st.file_uploader("📤 Upload a .wav meeting audio file", type=["wav"])

if uploaded:
    with open("meeting.wav", "wb") as f:
        f.write(uploaded.read())

    st.info("⏳ Transcribing audio...")
    raw_text = transcribe_audio("meeting.wav")
    st.subheader("🗒️ Full Transcript")
    st.text(raw_text)

    st.info("🧠 Summarizing...")
    summary = generate_summary(raw_text)
    st.subheader("📄 Summary")
    st.success(summary)

    st.info("✅ Extracting Action Items...")
    actions = extract_action_items(raw_text)
    st.subheader("🔖 Action Items")
    for item in actions:
        st.write("- ", item)

    with open("summary.txt", "w") as sfile:
        sfile.write(summary)

    with open("action_items.txt", "w") as afile:
        afile.write("\n".join(actions))

    st.download_button("📥 Download Summary", data=summary, file_name="summary.txt")
    st.download_button("📥 Download Action Items", data="\n".join(actions), file_name="action_items.txt")
