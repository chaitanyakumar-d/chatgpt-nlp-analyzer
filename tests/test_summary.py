import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from scripts.chatgpt_utils import summarize_text

def test_summary():
    sample = "OpenAI developed ChatGPT to assist with various tasks."
    summary = summarize_text(sample)
    assert isinstance(summary, str)
    assert len(summary) > 10

