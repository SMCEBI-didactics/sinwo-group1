from WebApp import app
from flask import render_template

"""
"""

@app.route("/")
def home_route():
    """
    """
    return render_template("index.html")

@app.route("/api/<var>")
def api_route(var):
    """
    """
    return render_template("api.html", var=var)

@app.route("/login", methods=["GET", "POST"])
def login_route():
    """
    """
    state = "Unauthenticated"
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        state = f"{state} {login}:{password}"
    return render_template("login.html", state=state)
