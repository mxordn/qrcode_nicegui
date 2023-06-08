FROM zauberzeug/nicegui:latest

WORKDIR /app

COPY *.py .
COPY start.sh .
COPY requirements-docker.txt .

RUN pip install -r requirements-docker.txt
