# WebApp
ŚiNWO Aplikacja bazowa

### Instalacja zależności:

Użyj wirtualnego środowiska:

```console
user@host:~$ virtualenv flask_venv
user@host:~$ source flask_venv/bin/activate
(flask_venv) user@host:~$ pip install -r requirements.txt

```

### Użycie:



```console
user@host:~$ python app.py #działa na zdefiniowanym w app.py adresie o porcie
```

lub


```console
# ustawienie zmiennych środowiskowych
(flask_venv) user@host:~$ export FLASK_APP=app.py 
(flask_venv) user@host:~$ export FLASK_ENV=development
#uruchomienie na wszystkich interfejsach i porcie 9999
(flask_venv) user@host:~$ flask run -h 0.0.0.0 -p 9999
```

adres oraz port może być również zdefiniowany przezzmienne środowiskowe:

```console
(flask_venv) user@host:~$ export FLASK_RUN_HOST=0.0.0.0
(flask_venv) user@host:~$ export FLASK_RUN_PORT=9999
```
