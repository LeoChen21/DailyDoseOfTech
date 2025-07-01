import feedparser
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
from typing import List, Dict
from config import NEWS_SOURCES, AI_KEYWORDS, MAX_ARTICLES_PER_SOURCE

class NewsAggregator:
    def __init__(self):
        self.articles = []
        
    def fetch_rss_feed(self, url: str) -> List[Dict]:
        try:
            feed = feedparser.parse(url)
            articles = []
            
            for entry in feed.entries[:MAX_ARTICLES_PER_SOURCE]:
                article = {
                    'title': entry.title,
                    'link': entry.link,
                    'published': entry.get('published', ''),
                    'summary': entry.get('summary', ''),
                    'source': feed.feed.get('title', 'Unknown Source')
                }
                articles.append(article)
            
            return articles
        except Exception as e:
            print(f"Error fetching RSS feed {url}: {e}")
            return []
    
    def is_ai_related(self, text: str) -> bool:
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in AI_KEYWORDS)
    
    def filter_ai_articles(self, articles: List[Dict]) -> List[Dict]:
        ai_articles = []
        for article in articles:
            title_summary = f"{article['title']} {article['summary']}"
            if self.is_ai_related(title_summary):
                ai_articles.append(article)
        return ai_articles
    
    def is_recent(self, published_date: str, days_back: int = 1) -> bool:
        try:
            from dateutil import parser
            article_date = parser.parse(published_date)
            cutoff_date = datetime.now() - timedelta(days=days_back)
            return article_date.replace(tzinfo=None) >= cutoff_date
        except:
            return True
    
    def aggregate_news(self) -> List[Dict]:
        all_articles = []
        
        for source_url in NEWS_SOURCES:
            print(f"Fetching from: {source_url}")
            articles = self.fetch_rss_feed(source_url)
            ai_articles = self.filter_ai_articles(articles)
            
            recent_articles = [
                article for article in ai_articles 
                if self.is_recent(article.get('published', ''))
            ]
            
            all_articles.extend(recent_articles)
        
        seen_titles = set()
        unique_articles = []
        for article in all_articles:
            title_clean = re.sub(r'[^\w\s]', '', article['title'].lower())
            if title_clean not in seen_titles:
                seen_titles.add(title_clean)
                unique_articles.append(article)
        
        return sorted(unique_articles, key=lambda x: x.get('published', ''), reverse=True)
    
    def get_latest_news(self) -> List[Dict]:
        return self.aggregate_news()

if __name__ == "__main__":
    aggregator = NewsAggregator()
    articles = aggregator.get_latest_news()
    
    print(f"Found {len(articles)} AI-related articles:")
    for article in articles[:10]:
        print(f"- {article['title']}")
        print(f"  Source: {article['source']}")
        print(f"  Link: {article['link']}")
        print()