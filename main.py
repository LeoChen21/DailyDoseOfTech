#!/usr/bin/env python3

import schedule
import time
import argparse
from datetime import datetime
from news_aggregator import NewsAggregator
from ai_summarizer import AISummarizer
from email_sender import EmailSender

class DailyDoseBot:
    def __init__(self):
        self.aggregator = NewsAggregator()
        self.summarizer = AISummarizer()
        self.email_sender = EmailSender()
    
    def run_daily_digest(self):
        print(f"🤖 Starting Daily Dose of Tech - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        try:
            print("📰 Aggregating latest AI news...")
            articles = self.aggregator.get_latest_news()
            
            if not articles:
                print("❌ No new articles found today.")
                return
            
            print(f"✅ Found {len(articles)} articles")
            
            print("🧠 Generating AI summaries and categorizing...")
            for article in articles:
                article['ai_summary'] = self.summarizer.summarize_article(article)
            
            intro = self.summarizer.generate_newsletter_intro(len(articles))
            categories = self.summarizer.categorize_articles(articles)
            
            print("📧 Sending email newsletter...")
            success = self.email_sender.send_email(articles, intro, categories)
            
            if success:
                print("✅ Daily digest sent successfully!")
            else:
                print("❌ Failed to send email. Check your configuration.")
                
        except Exception as e:
            print(f"❌ Error in daily digest: {e}")
    
    def preview_digest(self):
        print("🔍 Generating preview of today's digest...")
        
        articles = self.aggregator.get_latest_news()
        
        if not articles:
            print("❌ No articles found for preview.")
            return
        
        for article in articles[:5]:
            article['ai_summary'] = self.summarizer.summarize_article(article)
        
        intro = self.summarizer.generate_newsletter_intro(len(articles))
        categories = self.summarizer.categorize_articles(articles[:5])
        
        self.email_sender.preview_email(articles[:5], intro, categories)
        
        print(f"\\n📊 Summary:")
        print(f"Total articles found: {len(articles)}")
        print(f"Categories: {list(categories.keys())}")
    
    def schedule_daily_run(self, time_str: str = "08:00"):
        print(f"⏰ Scheduling daily digest for {time_str}")
        schedule.every().day.at(time_str).do(self.run_daily_digest)
        
        print("🚀 Bot is running! Press Ctrl+C to stop.")
        print(f"Next run scheduled for: {schedule.next_run()}")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            print("\\n👋 Bot stopped by user.")

def main():
    parser = argparse.ArgumentParser(description='Daily Dose of Tech - AI News Bot')
    parser.add_argument('--run', action='store_true', help='Run the digest once now')
    parser.add_argument('--preview', action='store_true', help='Preview the digest without sending')
    parser.add_argument('--schedule', type=str, help='Schedule daily runs (format: HH:MM, default: 08:00)')
    parser.add_argument('--daemon', action='store_true', help='Run as daemon with default schedule')
    
    args = parser.parse_args()
    
    bot = DailyDoseBot()
    
    if args.run:
        bot.run_daily_digest()
    elif args.preview:
        bot.preview_digest()
    elif args.schedule:
        bot.schedule_daily_run(args.schedule)
    elif args.daemon:
        bot.schedule_daily_run()
    else:
        print("🤖 Daily Dose of Tech - AI News Bot")
        print("\\nUsage:")
        print("  python main.py --run          # Run digest once now")
        print("  python main.py --preview      # Preview digest without sending")
        print("  python main.py --schedule 09:30  # Schedule daily runs at 9:30 AM")
        print("  python main.py --daemon       # Run as daemon (default: 8:00 AM)")
        print("\\nMake sure to configure your .env file first!")

if __name__ == "__main__":
    main()