SHELL := /bin/bash
all:
	echo "test, update-db, clear, run"
test:
	source tests/start_tests

update-db:
	source tests/update_db

clear:
	rm -rf venv/
	rm -rf flask-venv/

run:
	virtualenv venv
	source venv/bin/activate
	pip install -r requirements.txt
	export FLASK_APP=app.py
	export FLASK_ENV=development
	flask run -h 0.0.0.0 -p 9999