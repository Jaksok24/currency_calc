import requests

url = "https://api.nbp.pl/api/exchangerates/tables/A/"
response = requests.get(url)

def Calc():
    print('---KALKULATOR WALUT---\n')
    while True:
        choice = input('Wybierz walute\n1.Dolar amerykański\n2.Euro\n3.Wyjdź\n')
        match choice:
            case '1':
                num = int(input('Podaj kwote do przeliczenia: '))
                print(f"\n{num} USD kosztuje {round(num*usd, 2)} PLN\n")
            case '2':
                num = int(input('Podaj kwote do przeliczenia: '))
                print(f"\n{num} EUR kosztuje {round(num*eur, 2)} PLN\n")
            case '3':
                break
            case _:
                print('Wprowadź odpowiednią opcję\n')

if response.status_code == 200:
    data = response.json()
    for rate in data[0]['rates']:
        if rate['code'] == 'USD':
            usd = rate['mid']
        if rate['code'] == 'EUR':
            eur = rate['mid']
else:
    print(f"Błąd: {response.status_code}")

Calc()
