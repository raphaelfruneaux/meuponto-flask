FROM python:3.6

RUN apt-get update \
    && apt-get -y install unzip \
    && apt-get -y install libaio-dev \
    && mkdir -p /opt/data

WORKDIR /opt/data

EXPOSE 5000

COPY requirements.txt requirements.txt
COPY requirements.prod.txt requirements.prod.txt

RUN pip install -r requirements.prod.txt


CMD ["gunicorn", "run:app", "--name meupont-api", "--workers 3", "--bind 0.0.0.0:5000"]