FROM python:3.8-slim

RUN pip install fastapi uvicorn mongoengine dnspython

EXPOSE 1995

COPY . /app
WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1995"]