FROM python:3.10-slim

WORKDIR /app

# Instalăm dependențele necesare
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiem tot codul aplicației în container
COPY . /app

# Expunem portul 7860 pentru Gradio
EXPOSE 7860

# Comanda de pornire
CMD ["python", "app.py"]
