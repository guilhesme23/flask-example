FROM python:3.6

WORKDIR /flask-example

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

CMD python server.py