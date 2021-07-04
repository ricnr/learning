FROM python:3.8-slim-buster

COPY ./service /service
WORKDIR /service

RUN pip3 install -r ./requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
