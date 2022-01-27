from Rock_paper import runRock

def main(x):
    """ Funkcja zwracająca funkcję obsługującą grę "Kamień, papier, nożyce".
    
        Args:
            x (int): Wybór gracza.

        Returns:
            str: Rezultat gry.

    """
    return runRock(x)

if __name__ == "__main__":
    main()
