import urllib.request
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate  # курс обмена для 1 вашей валюты в долларах США

    def convert_to_usd(self, amount_in_local_currency):
        return amount_in_local_currency / self.exchange_rate


def fetch_exchange_rate():
    url = "https://www.oenb.at/en/Monetary-Policy/Exchange-rates.html"  # URL с курсами валют

    # Получаем данные с сайта через urllib
    with urllib.request.urlopen(url) as response:
        page = response.read()

    soup = BeautifulSoup(page, "html.parser")

    # Ищем строку с валютой USD
    rows = soup.find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        if len(columns) >= 3 and columns[0].text.strip() == "US-Dollar" and columns[1].text.strip() == "USD":
            # Извлекаем курс из третьей колонки
            rate = columns[2].text.strip()
            return float(rate.replace(",", "."))  # заменяем запятую на точку для корректного преобразования в float

    raise ValueError("Не удалось найти курс доллара США.")


if __name__ == "__main__":
    try:
        exchange_rate = fetch_exchange_rate()
        print(f"Курс доллара США: {exchange_rate} местной валюты за 1 USD")

        amount_in_local_currency = float(input("Введите количество вашей валюты: "))
        converter = CurrencyConverter(exchange_rate)
        amount_in_usd = converter.convert_to_usd(amount_in_local_currency)
        print(f"Соответствующая сумма в долларах США: {amount_in_usd:.2f} USD")

    except Exception as e:
        print(f"Ошибка: {e}")
