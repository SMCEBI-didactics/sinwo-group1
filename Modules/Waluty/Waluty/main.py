import click

def Przeliczwaluty(Ilosc,Waluta):
    """
    Funkcja przelicza wybraną walutę na PLN

    Attributes:
        ilosc : Ile pieniędzy
        waluta :  Wybór waluty

    """
    wynik= None
    if Waluta =="eur" or Waluta =="EUR":
        wynik = int(Ilosc) / 4.2999
    elif Waluta == "gbp" or Waluta == "GBP":
        wynik = int(Ilosc) / 5.0272
    elif Waluta == "usd" or Waluta == "USD":
        wynik = int(Ilosc) / 3.8232
    elif Waluta == "aud" or Waluta == "AUD":
        wynik = int(Ilosc) / 2.6994
    else:
        print("Error: Sproboj jeszcze raz.")
    return wynik
@click.command()
@click.option("--Ilosc", type=float, prompt="Podaj liczbę")
@click.option("--Waluta", type=str, prompt="Jaka waluta")
def main(Ilosc, Waluta):
    wynik = Przeliczwaluty(Ilosc, Waluta)
    print(f"Wynik: {Ilosc}/{Waluta}={wynik}")
    return None

if __name__ == "__main__":
    main()
