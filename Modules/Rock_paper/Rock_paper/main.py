from Rock_paper import runRock

def main(x):
    """ Funkcja zwracająca funkcję obsługującą grę "Kamień, papier, nożyce".
    
        Parameters:
            x int: Wybór gracza.

        Returns:
            String

    """
    return runRock(x)

if __name__ == "__main__":
    main()
