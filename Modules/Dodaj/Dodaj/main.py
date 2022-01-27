import click

def dodaj(a,b):
    """ Funkcja dodaje dwie liczby.

        Args:
            liczba1 (float): Liczba pierwsza.
            liczba2 (float): Liczba druga.

        Returns:
            float: Suma liczb.
    """
    return a+b

@click.command()
@click.option("--liczba1", help="podaj liczbe 1", prompt="podaj liczbę 1")
@click.option("--liczba2", help="podaj liczbe 2", prompt="Podaj liczbę 2")
def main(liczba1, liczba2):
    wynik = dodaj(liczba1, liczba2)
    print(f"Wynik: {liczba1}+{liczba2}={wynik}")
    return None

if __name__ == "__main__":
    main()
