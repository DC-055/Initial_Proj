FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN python -m pip install --no-cache-dir . pytest

CMD ["python", "-m", "pytest"]