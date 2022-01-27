from sqlalchemy import TEXT
from WebApp import app
from WebApp.models import *
from flask import render_template, request, make_response
from Dodaj.main import dodaj
from Calculator.main import compute
from Identity.main import gen_identity
from Rock_paper.main import runRock
from Tic_tac_toe.main import play_game
from Waluty.main import Przeliczwaluty

"""
"""


@app.route("/")
def home_route():
    """
    Strona główna
    """
    return render_template("home.html")

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    """
    Strona z kalkulatorem IP
    """
    if request.method == "GET":
        return render_template("calculator.html")
    else:
        a = request.form["address"]
        m = request.form["mask"]
        address, klasa, broadcast, range_up, range_down  = compute(a, m)
        return render_template("calculator.html", address = address, klasa = klasa, broadcast = broadcast, range_up = range_up, range_down = range_down)

@app.route("/typing")
def typing():
    return render_template("typing.html")

@app.route("/reading")
def reading():
    return render_template("reading.html")


@app.route("/rock_paper", methods=["GET","POST"])
def rock_paper():
	""" Funkcja obslugujaca gre w kamien, papier, nozyce

	    Parameters:
		None

	    Returns:
		html file.
	"""
	if request.method == "POST":
		var = request.form.get("nm")
		return runRock(var)
	else:
		return render_template("rock_paper.html")


@app.route("/tic_tac", methods=["GET", "POST"])
def tic_tac():
    cookie = request.cookies.get("game_board")
    var = request.form
    t, msg = play_game(cookie, var)
    resp = make_response(render_template("tic_tac.html", t=t, msg=msg))
    c = ",".join(map(str, t.board))
    resp.set_cookie("game_board", c)
    return resp

@app.route("/Przeliczwaluty", methods=["GET","POST"])
def Przeliczwalute(): 
    """ 
    Funkcja przelicza wybraną walutę na PLN
    """
    status= "Ile pieniędzy"
    if request.method == "POST":
        Waluta = request.form["Waluty"]
        Ilosc = request.form["Ilosc"]
        wynik = Przeliczwaluty(float(Ilosc),Waluta)
        status=f"Wynik = {wynik}"
        print("Wynik = ",wynik)
    return render_template("waluty.html",status = status)


#######################
#######################
#######################
#   Przykłady użycia  #
# praca z bazą danych #
#######################

@app.route("/przyklad", methods=["GET", "POST"])
def przyklad():
    """
    Przykład: dodawanie 2 liczb
    """
    # pobranie zawartości liczb
    status = "Oczekiwanie na liczby"
    if request.method == "POST":
        liczba1 = request.form["liczba1"]
        liczba2 = request.form["liczba2"]

        #  osobny moduł (funkcjonalność), Patrz Modules/Dodaj
        wynik = dodaj(float(liczba1), float(liczba2))
        status = f"{liczba1} + {liczba2} = {wynik}"

        # komunikacja z bazą; dodanie wyniku do bazy
        db_wynik = Dodawanie(liczba1=liczba1, liczba2=liczba2, wynik=wynik)
        try:
            db.session.add(db_wynik)
            db.session.commit()
        except Exception as e:
            print(f"Błąd podczas dodawania wyniku do bazy \n{e}")

    # komunikacja z bazą: pobieranie zawartości tablicy
    stare_wyniki = Dodawanie.query.filter().all() 
    # zwraca tablice obiektów, zamiast all() można użyć first() (pierwszy obiekt), 
    # dostęp do zawartości przez np. stare_wyniki[1].liczba1. 
    # Aby dodać warunek można użyć: Dodawanie.query.filter(Dodawanie.wynik=="3.0").first()

    #################################################
    # Aktualizacja zawartości bazy możliwa przez:
    #   wpis = Dodawanie.query.filter(id==3).first() # istnieje również metoda one()
    #   wpis.liczba1 = 111
    #   wpis.liczba2 = 999
    #   db.session.commit()
    #################################################
    # Usuwanie wpisów z bazy: 
    #   wpis = Dodawanie.query.filter(id==3).first()
    #   db.session.delete(wpis) #używaj try:
    #   db.session.commit()
    #################################################

    return render_template("dodawanie.html", status=status, stare_wyniki=stare_wyniki)



##################
# inne przykłady #
##################

@app.route("/api/<var>")
def api_route(var):
    """
    przykład adres:port/api/cos
    """
    return render_template("api.html", var=var)

@app.route("/loginbeta", methods=["GET", "POST"])
def login_route():
    """
    przykład adres:port/loginbeta
    """
    state = "Unauthenticated"
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        state = f"{state} {login}:{password}"
    return render_template("login.html", state=state)


@app.route("/prompt", methods=["GET", "POST"])
def prompt():
    """
    testuj polecenia 
    """
    state = "empty"
    if request.method == "POST":
        prompt = request.form["prompt"]
        prompt = eval(prompt)
        state = f"{prompt}"
    return render_template("prompt.html", state=state)


@app.route("/identity", methods=["GET","POST"])
def identity():
    """
    testuj polecenia 
    """
    state = "empty"
    if request.method == "GET":
        state = f"{request.remote_addr}"
        return render_template("identity.html", state=state)
    if request.method == "POST":
        pesel,data_ur,miejce_zamieszkania,nr_telefonu,plec,kolor_wlosow,kolor_oczu = gen_identity()
        return render_template("identity.html", pesel = pesel, data_ur = data_ur,miejce_zamieszkania = miejce_zamieszkania, nr_telefonu = nr_telefonu, plec = plec, kolor_wlosow = kolor_wlosow, kolor_oczu = kolor_oczu)

if __name__=="__main__":
	app.run()

