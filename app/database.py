import sqlite3

def setup_database():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temp REAL,
        dt TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()
