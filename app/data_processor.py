from datetime import datetime
import sqlite3

class DataProcessor:
    def process_data(self, data, city):
        temp_celsius = data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
        # Store the processed data in the database
        self.store_data(city, temp_celsius, data)

    def store_data(self, city, temp, data):
        with sqlite3.connect('/app/weather.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO weather (city, temp, dt) VALUES (?, ?, ?)", 
                           (city, temp, datetime.fromtimestamp(data['dt'])))
            conn.commit()
