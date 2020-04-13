#FROM python:rc-windowsservercore
##python:3.7.2-slim
#
#COPY . /app
#WORKDIR /app
#
#RUN pip install --upgrade pip
#RUN pip install flask
#RUN pip install pyjwt
#RUN pip install gunicorn
#RUN pip install pytest
#
#ENTRYPOINT ["python", "main.py"]

FROM python:stretch

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "gunicorn", "-b", ":8080", "main:APP" ]