from WebApp import app
from flask import render_template, request

"""
"""

@app.route("/")
def home_route():
    """
    Strona główna
    """
    return render_template("index.html")





####################
# Przykłady użycia #
####################

@app.route("/temat2", methods=["GET", "POST"])
def temat2():
    """
    Przykład dodania 2 liczb
    """
    # pobranie zawartości liczb
    status = "Oczekiwanie na liczby"
    if request.method == "POST":
        liczba1 = request.form["liczba1"]
        liczba2 = request.form["liczba2"]
        wynik = float(liczba1) + float(liczba2)
        status = f"{liczba1} + {liczba2} = {wynik}"
        # komunikacja z bazą
    return render_template("dodawanie.html", status=status)

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


               


  


               

               

               

               
