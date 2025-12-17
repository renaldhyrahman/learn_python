import constant as const
import requests as req


# STEP 1
def get_delta_percentage(stock: str) -> float:
    url = const.API.ALPHAVANTAGE_API.value
    url += "/query"
    res = req.get(
        url=url,
        params={
            "function": "TIME_SERIES_DAILY",
            "symbol": stock,
            "apikey": const.API.ALPHAVANTAGE_TOKEN.value,
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
def get_news(query: str):
    url = const.API.NEWSAPI_API.value
    url += "/everything"
    res = req.get(
        url=url,
        params={
            "q": query,
            "apiKey": const.API.NEWSAPI_TOKEN.value,
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
def send_telegram(message: str):
    url = const.Telegram.BOT_API.value
    url += const.Telegram.BOT_TOKEN.value
    url += "/sendMessage"
    res = req.post(
        url=url,
        json={
            "chat_id": const.Telegram.CHAT_ID.value,
            "text": message,
        },
    )
    res.raise_for_status()


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds
and prominent investors are required to file by the SEC The 13F filings show
the funds' and investors' portfolio positions as of March 31st,
near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds
and prominent investors are required to file by the SEC The 13F filings show
the funds' and investors' portfolio positions as of March 31st,
near the height of the coronavirus market crash.
"""


def message_formatter(delta_stock: float, news: list[str, str]):
    pass


def app():
    delta = get_delta_percentage(const.STOCK)
    is_get_news = abs(delta) <= 0.05
    if not is_get_news:
        return
    news = get_news(const.COMPANY_NAME)
    message = "\n".join([article["title"] for article in news])
    send_telegram(message)


app()
