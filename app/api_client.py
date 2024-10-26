import requests
from config import Config

class WeatherAPIClient:
    def get_weather(self, city):
        params = {
            "q": city,
            "appid": Config.API_KEY,
        }
        response = requests.get(Config.API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching weather data: {response.status_code}")
