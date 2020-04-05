FROM python:rc-windowsservercore-ltsc2016

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]

