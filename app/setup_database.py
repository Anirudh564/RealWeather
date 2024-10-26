import sqlite3

def initialize_db():
    try:
        conn = sqlite3.connect("/app/weather.db")  # Use Docker-friendly path
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                temp REAL NOT NULL,
                dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

        # Print tables for debugging
        tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        print("Tables in database:", tables)

        if not tables:
            print("Warning: No tables found!")
        conn.close()
    except Exception as e:
        print("Error during database initialization:", e)

if __name__ == "__main__":
    initialize_db()
    print("Database initialized.")
