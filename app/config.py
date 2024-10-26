import os

class Config:
    API_KEY = os.getenv("OPENWEATHERMAP_API_KEY", "4d01256b89f4db3e8cfe1396f6988cc5")
    API_URL = "http://api.openweathermap.org/data/2.5/weather"
    METROS = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
    INTERVAL = 300  # Interval in seconds for data retrieval (5 minutes)
    ALERT_THRESHOLD_TEMP = 35  # Temperature threshold for alerts
