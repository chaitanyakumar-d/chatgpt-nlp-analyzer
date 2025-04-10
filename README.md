# 🧠 ChatGPT NLP Analyzer

A Streamlit-powered app that uses the OpenAI ChatGPT API to analyze and summarize PDF/text content. Upload documents, extract summaries and keywords, analyze sentiment, and ask questions conversationally — all powered by AI!


## 🔍 Features
- 📄 Upload PDF, DOCX or Audio
- 🧠 ChatGPT-powered summarization
- 📝 Keyword extraction & sentiment analysis
- 💬 Chat with your document
- 📥 Export results

## 🚀 Install & Run
```bash
git clone https://github.com/yourusername/chatgpt-nlp-analyzer.git
cd chatgpt-nlp-analyzer
python -m venv venv
source venv/bin/activate #This is Linux command for windows use windows command
pip install -r requirements.txt
cp .env.example .env  # or else Create a .env file at the root of your project:
# Add your OpenAI key
streamlit run app/app.py
```

## 📦 Tech Stack
- Streamlit
- OpenAI GPT
- Whisper
- PyMuPDF
- python-docx
- dotenv

## 🙌 Author
Built with ❤️ by [Chaitanya Kumar Dasari](https://github.com/chaitanyakumar-d)
