from config import Config

class AlertManager:
    def check_alerts(self, data, city):
        temp = data["main"]["temp"] - 273.15
        if temp > Config.ALERT_THRESHOLD_TEMP:
            print(f"Alert! Temperature in {city} has exceeded {Config.ALERT_THRESHOLD_TEMP}°C")
