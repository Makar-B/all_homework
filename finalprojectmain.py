import requests
from bs4 import BeautifulSoup
import sqlite3
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Клас DateWeather
class DateWeather:
    def __init__(self, date, temperature, precipitation, wind_speed, wind_direction):
        self.date = date
        self.temperature = temperature
        self.precipitation = precipitation
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction

    def __str__(self):
        return (f"Date: {self.date}, Temperature: {self.temperature}, "
                f"Precipitation: {self.precipitation}, Wind Speed: {self.wind_speed}, "
                f"Wind Direction: {self.wind_direction}")


# Функція для отримання даних з сайту
def fetch_weather_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        weather_data = []
        forecast_items = soup.find_all('div', class_='forecast-item')  # Замінити на реальний тег і клас сайту
        for item in forecast_items:
            date = item.find('span', class_='date').text.strip()
            temperature = item.find('span', class_='temperature').text.strip()
            precipitation = "Yes" if "rain" in item.find('span', class_='precipitation').text.lower() else "No"
            wind_speed = item.find('span', class_='wind-speed').text.strip()
            wind_direction = item.find('span', class_='wind-direction').text.strip()

            weather_data.append((date, temperature, precipitation, wind_speed, wind_direction))

        logging.info("Дані успішно отримано з сайту.")
        return weather_data

    except Exception as e:
        logging.error(f"Помилка при отриманні даних з сайту: {e}")
        return []


def initialize_database(db_name):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY,
                date TEXT,
                temperature TEXT,
                precipitation TEXT,
                wind_speed TEXT,
                wind_direction TEXT
            )
        ''')
        conn.commit()
        conn.close()
        logging.info("База даних успішно створена або вже існує.")
    except sqlite3.Error as e:
        logging.error(f"Помилка при створенні бази даних: {e}")


def save_weather_data(db_name, weather_data):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO weather (date, temperature, precipitation, wind_speed, wind_direction)
            VALUES (?, ?, ?, ?, ?)
        ''', weather_data)
        conn.commit()
        conn.close()
        logging.info("Дані успішно записані до бази даних.")
    except sqlite3.Error as e:
        logging.error(f"Помилка при записі до бази даних: {e}")


def fetch_from_database(db_name, condition):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        query = "SELECT * FROM weather WHERE " + condition
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        logging.info("Дані успішно вибрані з бази.")
        return results
    except sqlite3.Error as e:
        logging.error(f"Помилка при вибірці даних з бази: {e}")
        return []


def convert_to_dateweather(data):
    return [DateWeather(*row[1:]) for row in data]


if __name__ == "__main__":
    db_name = "weather.db"
    weather_url = "https://example.com/weather"

    initialize_database(db_name)

    weather_data = fetch_weather_data(weather_url)

    if weather_data:
        save_weather_data(db_name, weather_data)

    condition = "temperature = (SELECT MIN(temperature) FROM weather)"
    results = fetch_from_database(db_name, condition)

    date_weather_objects = convert_to_dateweather(results)
    for obj in date_weather_objects:
        print(obj)
