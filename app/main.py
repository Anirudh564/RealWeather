from api_client import WeatherAPIClient
from data_processor import DataProcessor
from alert_manager import AlertManager
from time import sleep
from config import Config

def run_weather_monitoring():
    client = WeatherAPIClient()
    processor = DataProcessor()
    alert_manager = AlertManager()
    
    while True:
        for city in Config.METROS:
            weather_data = client.get_weather(city)
            processor.process_data(weather_data, city)
            alert_manager.check_alerts(weather_data, city)
        sleep(Config.INTERVAL)

if __name__ == "__main__":
    run_weather_monitoring()
