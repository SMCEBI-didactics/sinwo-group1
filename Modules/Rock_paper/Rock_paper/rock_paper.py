import random


def runRock(x): 
    """ Funkcja obsługująca grę w "Kamień, papier, nożyce".

        Parameters:
            x int: Wybór gracza.

        Returns:
            String
    """
    var = int(x)
    en = random.randint(1,3)

    if var == 1:
        mr = "Kamień"
    elif var == 2:
        mr = "Papier"
    else:
        mr = "Nożyce"

    if en == 1:
        er = "Kamień"
    elif en == 2:
        er = "Papier"
    else:
        er = "Nożyce"

    if en==var:
        out = "REMIS"
    elif (en==1 and var == 2) or (en==2 and var==3) or (en==3 and var==1):
        out = "WYGRANA"
    else:
        out = "PRZEGRANA"
    return f"<h1>WYNIK:</h1><h3>Wybrales: {mr}, przeciwnik wybral: {er}</h3><br /><h1>{out}</h1>"


