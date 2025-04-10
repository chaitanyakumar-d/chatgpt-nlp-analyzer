from scripts.chatgpt_utils import summarize_text

def test_summary():
    sample = "OpenAI developed ChatGPT to assist with various tasks."
    summary = summarize_text(sample)
    assert isinstance(summary, str)
    assert len(summary) > 10

