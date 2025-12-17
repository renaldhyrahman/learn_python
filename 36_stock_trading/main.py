import constant as const
import requests as req


# STEP 1
def get_delta_percentage(stock: str) -> float:
    """
    Fetch daily stock prices and compute the percentage change
    between the two most recent trading days.

    Args:
        stock: Stock ticker symbol (e.g. "TSLA").

    Returns the percentage change from the previous trading day
    (positive for increase, negative for decrease).
    """
    endpoint = "/query"
    res = req.get(
        url=const.ALPHAVANTAGE_API + endpoint,
        params={
            "function": "TIME_SERIES_DAILY",
            "symbol": stock,
            "apikey": const.ALPHAVANTAGE_TOKEN,
        },
    )
    res.raise_for_status()
    data = res.json()["Time Series (Daily)"]
    dates = sorted(data.keys(), reverse=True)
    key_comparison = "4. close"
    yesterday = float(data[dates[0]][key_comparison])
    before_yesterday = float(data[dates[1]][key_comparison])
    return (yesterday - before_yesterday) / before_yesterday


# STEP 2
def get_news(query: str) -> list[dict[str, str]]:
    """
    Fetch the latest news articles matching a search query.

    Args:
        query (str): Search keyword or company name.

    Returns:
        list: A list of up to 3 news articles (dict),
              each containing 'title', 'description', and 'url'.
    """
    endpoint = "/everything"
    res = req.get(
        url=const.NEWSAPI_API + endpoint,
        params={
            "q": query,
            "apiKey": const.NEWSAPI_TOKEN,
        },
    )
    res.raise_for_status()
    data = res.json()["articles"][:3]
    return [
        {
            "title": news["title"],
            "description": news["description"],
            "url": news["url"],
        }
        for news in data
    ]


# STEP 3
def send_telegram(message: str) -> None:
    """
    Send a text message to a Telegram chat using a bot.

    Args:
        message: Message that will be sent.
    """
    url = const.TELEGRAM_BOT_API + const.TELEGRAM_BOT_TOKEN
    endpoint = "/sendMessage"
    res = req.post(
        url=url + endpoint,
        json={
            "chat_id": const.TELEGRAM_CHAT_ID,
            "text": message,
        },
    )
    res.raise_for_status()


# Optional:
def message_formatter(
    stock: str,
    delta: float,
    news: dict[str, str],
) -> str:
    """
    Format a stock alert message including price movement and news.

    Args:
        stock: Stock ticker symbol.
        delta: Percentage price change.
        news: News article with keys
              'title', 'description', and 'url'.

    Returns a formatted message ready to be sent.
    """
    msg = f"{stock}: "
    if delta > 0:
        msg += "🔺"
    else:
        msg += "🔻"
    msg += f"{round(abs(delta) * 100, 2)}%\n\n"
    msg += f"Headline: {news['title']}\n\n"
    msg += f"Brief: {news['description']}\n\n"
    msg += f"Source: {news['url']}\n\n"
    return msg


# ######################    APP   ######################


def stock_notifier(equity: str, company: str, threshold: float) -> None:
    """
    Monitor a stock and send Telegram alerts with related news
    when the price change exceeds a given threshold.

    Args:
        equity: Stock ticker symbol.
        company: Company name used for news search.
        threshold: Percentage change required to trigger alerts.
    """
    delta = get_delta_percentage(equity)
    if abs(delta) <= threshold:
        print(f"{equity}: {round(delta * 100, 2)}%")
        return
    for news in get_news(company):
        message = message_formatter(equity, delta, news)
        send_telegram(message)


stock_notifier(
    equity=const.STOCK,
    company=const.COMPANY_NAME,
    threshold=0.05,
)
