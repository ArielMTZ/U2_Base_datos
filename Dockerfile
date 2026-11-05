FROM python:3.12-slim

WORKDIR /app

COPY Calculadora/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY Calculadora/ .

CMD ["python", "-m", "pytest", "-q"]