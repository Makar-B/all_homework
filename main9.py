import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime


def create_database():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_time TEXT,
            temperature TEXT
        )
    """)
    conn.commit()
    conn.close()


def fetch_weather():
    url = "https://meteofor.com.ua/ru/weather-vienna-2911/"  # Укажите URL сайта с погодой
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    req = urlopen(url)
    page = req.read().decode('utf-8')

    soup = BeautifulSoup(page, "html.parser")
    temp_element = soup.find("div", class_="temperature-class")
    return temp_element.text.strip() if temp_element else "N/A"


def insert_weather_data(temperature):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO weather_data (date_time, temperature) VALUES (?, ?)", (current_time, temperature))
    conn.commit()
    conn.close()


def read_weather_data():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather_data")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()


if __name__ == "__main__":
    create_database()
    try:
        temperature = fetch_weather()
        insert_weather_data(temperature)
        print("Температура успешно добавлена в базу данных!")
    except Exception as e:
        print(f"Ошибка: {e}")
    read_weather_data()
