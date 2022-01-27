FROM python:latest

COPY . identity

WORKDIR /identity/

#RUN pip install -r requirements.txt
RUN pip install .

ENTRYPOINT ["identity"]

