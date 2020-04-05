FROM 3.9.0a5-alpine3.10

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]

