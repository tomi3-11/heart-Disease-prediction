FROM python:3.11-slim

COPY requirements.txt .

RUN apt-get update && \
    python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
