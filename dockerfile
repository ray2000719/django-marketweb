FROM python:3.10.6

COPY . /marketAPP

WORKDIR /marketAPP

RUN pip install -r requirements.txt