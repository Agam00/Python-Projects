import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
LAT = os.getenv("LAT")
LON = os.getenv("LON")

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 7
}

def telegram_bot_sendtext(bot_message):
    send_text = (
        f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        f'?chat_id={BOT_CHAT_ID}&parse_mode=Markdown&text={bot_message}'
    )
    response = requests.get(send_text)
    return response.json()

# Fetch weather data
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

# Check if it will rain
will_rain = any(int(hour_data["weather"][0]["id"]) < 700 for hour_data in weather_data["list"])

# Send message
message = "It's going to rain today. Remember to bring an ☔" if will_rain else "No Rain Today"
result = telegram_bot_sendtext(message)
print(result)
