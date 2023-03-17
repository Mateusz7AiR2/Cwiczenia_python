from requests import get

print("KALKULATOR WALUT")
waluta = input("Podaj walutę: ")

data = input("Podaj datę (RRRR-MM-DD): ")

odpowiedz = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{data}/?format=json")

dane = odpowiedz.json()

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs:.3f} PLN")