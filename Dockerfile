FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . /app

# --no-cache-dir
# docker-compose up

CMD ["python3", "./run.py"]
