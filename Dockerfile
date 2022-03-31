FROM python:3.10.2-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
CMD ["cd", "help", "&&", "python3", "./manage.py runserver 0:8080"]