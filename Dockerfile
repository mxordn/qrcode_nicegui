FROM zauberzeug/nicegui:latest

WORKDIR /app

COPY main.py .
COPY qr_code_helpers.py .
COPY requirements-docker.txt .


RUN pip install -r requirements-docker.txt
