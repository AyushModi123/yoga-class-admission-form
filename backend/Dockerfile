FROM python:3.11-slim
WORKDIR /app
COPY . /app
COPY .dockerignore /app/.dockerignore
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
