import streamlit as st
import whisper
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import uuid

st.set_page_config(page_title="AI Video Editor", layout="wide")

model = whisper.load_model("base")
UPLOAD_DIR = "uploaded_videos"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("🎬 AI Video Editor for Creators")
st.write("Upload multiple takes of the same script. Transcribe, select best takes, and merge them!")

uploaded_files = st.file_uploader(
    "Upload your video files (.mp4, .mov)",
    type=["mp4", "mov"],
    accept_multiple_files=True
)

if uploaded_files:
    videos_data = []
    for uploaded_file in uploaded_files:
        file_id = str(uuid.uuid4())
        file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{uploaded_file.name}")
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        st.info(f"Transcribing: {uploaded_file.name}...")
        result = model.transcribe(file_path)
        segments = result["segments"]
        videos_data.append({"path": file_path, "segments": segments, "name": uploaded_file.name})

    st.success("Transcription complete.")

    selected_clips = []
    for vid in videos_data:
        st.subheader(f"🎥 {vid['name']}")
        for i, seg in enumerate(vid["segments"]):
            col1, col2 = st.columns([6, 1])
            with col1:
                st.write(f"{seg['start']:.2f}–{seg['end']:.2f}: {seg['text']}")
            with col2:
                if st.checkbox("✔️", key=f"{vid['name']}_{i}"):
                    selected_clips.append((vid["path"], seg["start"], seg["end"]))

    if selected_clips and st.button("Generate Final Video"):
        final_clips = []
        for path, start, end in selected_clips:
            clip = VideoFileClip(path).subclip(start, end)
            final_clips.append(clip)

        final = concatenate_videoclips(final_clips, method="compose")
        output = "final_video.mp4"
        final.write_videofile(output, codec="libx264")

        st.video(output)
        with open(output, "rb") as f:
            st.download_button("Download Video", f, file_name=output)
