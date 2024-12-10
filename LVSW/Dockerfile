# Basis-Image
FROM python:3.10-slim

# Arbeitsverzeichnis erstellen
WORKDIR /app

# Systembibliotheken installieren
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    gcc \
    && apt-get clean

# Abhängigkeiten kopieren
COPY LVSW/requirements.txt /app/

# Python-Abhängigkeiten installieren
RUN pip install --no-cache-dir -r requirements.txt

# Projektcode kopieren
COPY LVSW/ /app/

# Umgebungsvariablen setzen
ENV PYTHONUNBUFFERED=1

# Port für die Anwendung freigeben
EXPOSE 8000

# Kommando für den Start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
