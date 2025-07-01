import os
from dotenv import load_dotenv

load_dotenv()

NEWS_SOURCES = [
    "https://feeds.feedburner.com/oreilly/radar",
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
    "https://venturebeat.com/category/ai/feed/",
    "https://www.wired.com/feed/tag/ai/latest/rss",
    "https://www.artificialintelligence-news.com/feed/",
    "https://feeds.feedburner.com/kdnuggets-data-mining-analytics"
]

AI_KEYWORDS = [
    "artificial intelligence", "machine learning", "deep learning", "neural network",
    "chatgpt", "openai", "anthropic", "claude", "llm", "large language model",
    "generative ai", "gpt", "transformer", "bert", "nlp", "computer vision",
    "reinforcement learning", "pytorch", "tensorflow", "ai research", "ai safety",
    "automation", "robotics", "ai ethics", "ai regulation", "ai startup"
]

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))

MAX_ARTICLES_PER_SOURCE = 5
MAX_SUMMARY_LENGTH = 150