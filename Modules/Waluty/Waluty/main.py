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
        wynik = int(Ilosc) / 4.57
    elif Waluta == "gbp" or Waluta == "GBP":
        wynik = int(Ilosc) / 5.48
    elif Waluta == "usd" or Waluta == "USD":
        wynik = int(Ilosc) / 4.08
    elif Waluta == "aud" or Waluta == "AUD":
        wynik = int(Ilosc) / 2.90
    elif Waluta == "chf" or Waluta == "CHF":
        wynik = int(Ilosc) / 4.3872
    elif Waluta == "ars" or Waluta == "ARS":
        wynik = int(Ilosc) / 0.04   
    elif Waluta == "hrk" or Waluta == "HRK":
        wynik = int(Ilosc) / 0.61
    elif Waluta == "jpy" or Waluta == "JPY":
        wynik = int(Ilosc) / 0.04
    elif Waluta == "mxn" or Waluta == "MXN":
        wynik = int(Ilosc) / 0.20               
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
