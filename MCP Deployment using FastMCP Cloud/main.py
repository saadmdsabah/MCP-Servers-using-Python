import feedparser
from fastmcp import FastMCP

mcp = FastMCP("Google News Parser")


@mcp.tool(
    name="Google News Feed Parser",
    description="Get the latest headlines and metadata from the Google News RSS feed.",
    tags={"google news", "news feed"},
)
def get_google_news_feed(max_results: int = 3):
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
                "description": entry.get("description"),
                "source": entry.get("source"),
                "pubDate": entry.get("published"),
            }
        )

    return results


if __name__ == "__main__":
    mcp.run(transport="http")
