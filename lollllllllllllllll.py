import requests
import re

class CurrencyConverter:
    def __init__(self, url):
        self.url = url
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        response = requests.get(self.url)
        response.raise_for_status()

        match = re.search(r'<td>USD</td>\s*<td>\d+</td>\s*<td>[\d,]+</td>\s*<td>([\d,]+)</td>', response.text)
        if match:
            return float(match.group(1).replace(",", "."))  # Извлекаем курс USD

        raise ValueError("Не удалось найти курс доллара на сайте")

    def convert(self, amount):
        return round(amount / self.exchange_rate, 2)

if __name__ == "__main__":
    url = "https://www.cbr.ru/currency_base/daily/"
    
    try:
        converter = CurrencyConverter(url)
        amount = float(input("Введите сумму в вашей валюте: "))
        usd_amount = converter.convert(amount)
        print(f"Эквивалент в долларах США: ${usd_amount}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except requests.RequestException:
        print("Ошибка подключения к сайту банка")
