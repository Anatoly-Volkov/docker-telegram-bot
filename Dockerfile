FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y \
    python3 \
    python3-pip

RUN pip3 install pyTelegramBotApi
COPY images images
COP source.py source.py

CMD ["python3", "source.py"]
 
