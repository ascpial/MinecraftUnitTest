FROM openjdk:17-jdk-buster

RUN apt-get update; \
    apt-get install -y python3 python3-pip; \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "./docker-entrypoint.sh" ]