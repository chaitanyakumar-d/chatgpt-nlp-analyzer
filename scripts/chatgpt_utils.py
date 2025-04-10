import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatgpt_prompt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

def summarize_text(text):
    return chatgpt_prompt("Summarize the following text:\n" + text)

def extract_keywords(text):
    return chatgpt_prompt("Extract the main keywords from the following text:\n" + text)

def analyze_sentiment(text):
    return chatgpt_prompt("Analyze the sentiment of the following text (positive, neutral, negative):\n" + text)

def ask_question_from_text(text, question):
    return chatgpt_prompt(f"Answer the following question based on the text:\nText: {text}\nQuestion: {question}")

