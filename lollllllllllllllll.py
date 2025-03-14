import requests
import re
"""""НЕ СМОГ НАЙТИ САИТ("""
class CurrencyConverter:
    def __init__(self, url):
        self.url = url
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        response = requests.get(self.url)
        response.raise_for_status() 

        match = re.search(r'USD.*?(\d+,\d+)', response.text)
        if match:
            rate = match.group(1).replace(",", ".") 
            return float(rate)
        else:
            raise ValueError("Не удалось найти курс доллара на сайте")

    def convert(self, amount):
        return round(amount / self.exchange_rate, 2)

if __name__ == "__main__":
    url = "не нашел подходящего сайта" 
    converter = CurrencyConverter(url)

    try:
        amount = float(input("Введите сумму в вашей валюте: "))
        usd_amount = converter.convert(amount)
        print(f"Эквивалент в долларах США: ${usd_amount}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except requests.RequestException:
        print("Ошибка подключения к сайту банка")

