import feedparser
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI(title="Google News Feed Parser")


@app.get("/")
def home():
    return {"message": "Hello World!"}


@app.get("/feed")
def getFeed(max_results: int = 3):
    """
    name: "get_google_news_feed"
    description: "Get the latest headlines and metadata from the Google News RSS feed."
    tags: {"news", "google", "feed", "rss", "headlines"}
    Args:
        max_results (int): The maximum number of articles to return from the news feed.
    Returns:
        list: A list of news articles with title, url, description, source, and publication date.
    """
    parsed = feedparser.parse("https://news.google.com/rss")
    results = []

    for entry in parsed.entries[:max_results]:
        results.append(
            {
                "title": entry.get("title"),
                "url": entry.get("link"),
                "Description": entry.get("description"),
                "source": entry.get("source"),
                "pubDate": entry.get("published"),
            }
        )

    return results


mcp = FastApiMCP(app, name="Google News Parser")
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8081)
