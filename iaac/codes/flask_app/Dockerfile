FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN pip3 install --upgrade pip

COPY ./service /service
WORKDIR /service

RUN pip3 install -r ./requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
