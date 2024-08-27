FROM python:3.12-bullseye

RUN mkdir /code
WORKDIR /code

COPY ["./requirements.txt", "/code/requirements.txt"]

RUN apt-get update
RUN apt-get install python3-pip --yes


RUN pip3 install -r requirements.txt
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

COPY ["./src", "."]

EXPOSE 8082
CMD python3 -m uvicorn main:app --port 8082 --host 0.0.0.0