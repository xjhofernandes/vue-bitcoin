FROM python:3.8-slim

RUN pip install fastapi uvicorn mongoengine dnspython

EXPOSE 80

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]