# 🌟 DreamVi — AI-Powered Video Editor for Creators

**DreamVi** (*Dream Video*) is an AI-assisted smart video editing tool designed for content creators, educators, influencers, and storytellers. DreamVi allows you to upload multiple takes of the same script, transcribe them with AI, and intelligently merge the best moments into a seamless final video — all with just a few clicks.

---

## ✨ Why DreamVi?

Creators often record multiple takes to get their message just right — but selecting and editing the best parts from each one can be time-consuming.

**DreamVi automates the editing process** using advanced speech-to-text and video processing tools, helping you save time and stay focused on creating.

---

## 🔧 Features

- 🎥 Upload multiple takes of a script
- 🧠 Transcribe speech into text using OpenAI Whisper
- 📝 View all segments with timestamps and transcripts
- ✅ Manually select the best clips per line (auto-selection coming soon!)
- 🎞️ Automatically merge selected clips into a smooth final video
- 📥 Preview and download your final export
- 🌐 Run locally in your browser using Streamlit

---

## 🛠️ Tech Stack

| Layer        | Tool / Library           |
|--------------|---------------------------|
| UI Framework | [Streamlit](https://streamlit.io/) |
| AI Model     | [Whisper by OpenAI](https://github.com/openai/whisper) |
| Video Tools  | [MoviePy](https://zulko.github.io/moviepy/), [FFmpeg](https://ffmpeg.org/) |
| Language     | Python 3.8+ |

---

## 🚀 Getting Started

### 🔩 Prerequisites

- Python 3.8 or later
- `ffmpeg` installed and added to your system path

### 📦 Installation

```bash
git clone https://github.com/yourusername/DreamVi.git
cd DreamVi
pip install -r requirements.txt


streamlit run app.py


DreamVi/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── uploaded_videos/        # Temporary folder for uploads
└── README.md
