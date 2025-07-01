# 📰 DailyDoseOfTech

> Your automated daily tech news digest delivered straight to your inbox

A Python-powered bot that aggregates the latest tech news from multiple sources, creates AI-generated summaries, and sends beautifully formatted newsletters to your email.

## ✨ Features

- 🔄 **Automated News Aggregation**: Pulls latest tech news from RSS feeds and web sources
- 🤖 **AI-Powered Summaries**: Uses Anthropic's Claude API to generate concise summaries
- 📧 **Email Delivery**: Sends formatted newsletters directly to your inbox
- ⏰ **Scheduled Execution**: Runs automatically at your preferred time
- 🎯 **Customizable Sources**: Easy to add or modify news sources

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Gmail account (or other SMTP email provider)
- Anthropic API key (optional, for AI summaries)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/LeoChen21/DailyDoseOfTech.git
   cd DailyDoseOfTech
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual credentials
   ```

4. **Run the bot**
   ```bash
   python main.py
   ```

## ⚙️ Configuration

Copy `.env.example` to `.env` and configure:

```env
# Email Configuration
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
RECIPIENT_EMAIL=recipient@example.com

# SMTP Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

# AI Configuration (Optional)
ANTHROPIC_API_KEY=your-anthropic-api-key
```

### Gmail Setup
1. Enable 2-factor authentication
2. Generate an [App Password](https://support.google.com/accounts/answer/185833)
3. Use the app password as `EMAIL_PASSWORD`

## 📋 Usage

### Run Once
```bash
python main.py --run-once
```

### Schedule Daily Execution
```bash
python main.py --schedule
```

### Run with Custom Time
```bash
python main.py --schedule --time "09:00"
```

## 🛠️ Project Structure

```
DailyDoseOfTech/
├── main.py              # Main application entry point
├── news_aggregator.py   # News collection and processing
├── ai_summarizer.py     # AI-powered content summarization
├── email_sender.py      # Email formatting and delivery
├── config.py           # Configuration management
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
└── README.md          # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Issues & Support

Found a bug or have a feature request? Please [open an issue](https://github.com/LeoChen21/DailyDoseOfTech/issues).

---

*Built with ❤️ by Leo Chen*
