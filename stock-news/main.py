import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


# ------------------ CONFIG ------------------ #
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API keys from environment variables
stock_api_key = os.environ.get("STOCK_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")

# Twilio credentials from environment variables
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")
twilio_from = os.environ.get("TWILIO_FROM")
my_whatsapp = os.environ.get("MY_WHATSAPP")

# ------------------ STOCK DATA ------------------ #
stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key
}

response = requests.get("https://www.alphavantage.co/query", params=stock_param)
response.raise_for_status()
data = response.json()

recent_date = list(data["Time Series (Daily)"])[0]
prev_date = list(data["Time Series (Daily)"])[1]

recent_stock = float(data["Time Series (Daily)"][recent_date]["4. close"])
prev_stock = float(data["Time Series (Daily)"][prev_date]["4. close"])
difference = recent_stock - prev_stock
percentage = (abs(difference) / prev_stock) * 100

# ------------------ NEWS DATA ------------------ #
news_param = {
    "apiKey": news_api_key,
    "qInTitle": COMPANY_NAME,
    "from": prev_date,
    "sortBy": "popularity"
}

news_response = requests.get("https://newsapi.org/v2/everything", params=news_param)
news_response.raise_for_status()
news_data = news_response.json()
articles = news_data.get("articles", [])

news_list = []
for article in articles:
    title = article.get("title")
    description = article.get("description")
    if title and description:
        news_list.append(f"Headline: {title}\nBrief: {description}")
    if len(news_list) == 3:
        break

# ------------------ SEND ALERT ------------------ #
client = Client(account_sid, auth_token)

change_symbol = "🔺" if difference > 0 else "🔻"

if not news_list:
    message = client.messages.create(
        from_=twilio_from,
        body=f"{STOCK_NAME}: {change_symbol}{round(percentage,2)}%\nNo news articles found.",
        to=my_whatsapp
    )
else:
    for news in news_list:
        message = client.messages.create(
            from_=twilio_from,
            body=f"{STOCK_NAME}: {change_symbol}{round(percentage,2)}%\n\n{news}",
            to=my_whatsapp
        )

print("Alerts sent successfully!")
