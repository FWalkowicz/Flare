FROM python:3.12-bullseye

COPY ["./requirements.txt", "."]

RUN apt-get update
RUN apt-get install python3-pip --yes

RUN pip3 install -r requirements.txt

COPY ["./src", "."]

EXPOSE 8081
CMD python3 -m uvicorn main:app --port 8081 --host 0.0.0.0