import feedparser

class DailySummary:
    def __init__(self, sources):
        self.sources = sources

    def fetch_news(self):
        news_items = []
        for source in self.sources:
            feed = feedparser.parse(source)
            for entry in feed.entries:
                news_items.append({
                    'title': entry.title,
                    'link': entry.link,
                    'published': entry.published
                })
        return news_items

    def generate_summary(self):
        news = self.fetch_news()
        summary = "Daily Summary\n\n"
        for item in news:
            summary += f"{item['title']}\n{item['link']}\nPublished on: {item['published']}\n\n"
        return summary

# Example usage
if __name__ == "__main__":
    sources = [
        'https://news.ycombinator.com/rss',
        'http://feeds.bbci.co.uk/news/world/rss.xml'
    ]
    
    summary_generator = DailySummary(sources)
    daily_summary = summary_generator.generate_summary()
    print(daily_summary)
