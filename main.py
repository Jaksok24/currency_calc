import requests

url = "https://api.nbp.pl/api/exchangerates/tables/A/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for rate in data[0]['rates']:
        if rate['code'] == 'USD':
            dolar = round(rate['mid'],2)
            print(f"Kurs dolara (USD): {dolar} PLN")

else:
    print(f"Błąd: {response.status_code}")
