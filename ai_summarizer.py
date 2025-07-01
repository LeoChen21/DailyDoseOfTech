import anthropic
from typing import List, Dict
from config import ANTHROPIC_API_KEY, MAX_SUMMARY_LENGTH

class AISummarizer:
    def __init__(self):
        if ANTHROPIC_API_KEY:
            self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        else:
            self.client = None
            print("Warning: ANTHROPIC_API_KEY not found. Summarization will be disabled.")
    
    def summarize_article(self, article: Dict) -> str:
        if not self.client:
            return article.get('summary', '')[:MAX_SUMMARY_LENGTH]
        
        try:
            prompt = f"""Summarize this AI/tech news article in 1-2 sentences (max {MAX_SUMMARY_LENGTH} characters):

Title: {article['title']}
Content: {article['summary']}

Focus on the key AI/tech developments and their significance."""
            
            response = self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=60,
                temperature=0.3,
                messages=[{"role": "user", "content": prompt}]
            )
            
            summary = response.content[0].text.strip()
            return summary[:MAX_SUMMARY_LENGTH]
            
        except Exception as e:
            print(f"Error summarizing article: {e}")
            return article.get('summary', '')[:MAX_SUMMARY_LENGTH]
    
    def generate_newsletter_intro(self, article_count: int) -> str:
        if not self.client:
            return f"Here are the latest {article_count} AI and tech news articles:"
        
        try:
            prompt = f"""Write a brief, engaging introduction for a daily AI/tech newsletter with {article_count} articles.
Keep it under 50 words and make it sound professional but friendly."""
            
            response = self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=70,
                temperature=0.7,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.content[0].text.strip()
            
        except Exception as e:
            print(f"Error generating intro: {e}")
            return f"Here are today's top {article_count} AI and technology news stories:"
    
    def categorize_articles(self, articles: List[Dict]) -> Dict[str, List[Dict]]:
        categories = {
            "AI Research & Development": [],
            "AI Products & Services": [],
            "AI Regulation & Ethics": [],
            "AI Startups & Funding": [],
            "General Tech News": []
        }
        
        for article in articles:
            title_summary = f"{article['title']} {article['summary']}".lower()
            
            if any(keyword in title_summary for keyword in ["research", "paper", "study", "breakthrough", "algorithm"]):
                categories["AI Research & Development"].append(article)
            elif any(keyword in title_summary for keyword in ["product", "launch", "release", "chatgpt", "claude", "service"]):
                categories["AI Products & Services"].append(article)
            elif any(keyword in title_summary for keyword in ["regulation", "ethics", "policy", "law", "government"]):
                categories["AI Regulation & Ethics"].append(article)
            elif any(keyword in title_summary for keyword in ["startup", "funding", "investment", "raise", "venture"]):
                categories["AI Startups & Funding"].append(article)
            else:
                categories["General Tech News"].append(article)
        
        return {k: v for k, v in categories.items() if v}

if __name__ == "__main__":
    from news_aggregator import NewsAggregator
    
    aggregator = NewsAggregator()
    articles = aggregator.get_latest_news()
    
    summarizer = AISummarizer()
    
    print("Testing summarization:")
    if articles:
        summary = summarizer.summarize_article(articles[0])
        print(f"Original: {articles[0]['summary'][:100]}...")
        print(f"Summary: {summary}")
    
    print(f"\nIntro: {summarizer.generate_newsletter_intro(len(articles))}")
    
    categories = summarizer.categorize_articles(articles)
    print(f"\nCategories: {list(categories.keys())}")