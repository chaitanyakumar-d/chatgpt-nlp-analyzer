import sys
import os

# Add the project root directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

# Now import your utils
from scripts.chatgpt_utils import summarize_text, extract_keywords, analyze_sentiment, ask_question_from_text

import streamlit as st
from scripts.chatgpt_utils import summarize_text, extract_keywords, analyze_sentiment, ask_question_from_text
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
load_dotenv()



st.set_page_config(page_title="ChatGPT NLP Analyzer", layout="wide")
st.title("🧠 ChatGPT NLP Analyzer")

source_text = ""

uploaded_file = st.file_uploader("Upload PDF, DOCX or Audio", type=["pdf", "docx", "mp3", "wav"])
if uploaded_file:
    if uploaded_file.type == "application/pdf":
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        source_text = "\n".join(page.get_text() for page in doc)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        import docx
        doc = docx.Document(uploaded_file)
        source_text = "\n".join([para.text for para in doc.paragraphs])
    elif uploaded_file.type in ["audio/mpeg", "audio/wav"]:
        import tempfile, whisper
        temp = tempfile.NamedTemporaryFile(delete=False)
        temp.write(uploaded_file.read())
        model = whisper.load_model("base")
        result = model.transcribe(temp.name)
        source_text = result['text']

custom_text = st.text_area("Or paste your own text here:", height=200)
if custom_text:
    source_text = custom_text

if source_text:
    with st.expander("📄 Source Text"):
        st.write(source_text)

    st.subheader("🧠 NLP Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Summary**")
        st.write(summarize_text(source_text))

    with col2:
        st.write("**Keywords**")
        st.write(extract_keywords(source_text))

    st.write("**Sentiment**")
    st.write(analyze_sentiment(source_text))

    st.subheader("💬 Ask Questions")
    question = st.text_input("Type your question about the text:")
    if question:
        st.write(ask_question_from_text(source_text, question))

    st.download_button("⬇️ Export Text", source_text, file_name="extracted_text.txt")

