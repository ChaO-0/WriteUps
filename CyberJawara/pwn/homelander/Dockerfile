FROM ubuntu:latest

RUN apt update && \
    apt install socat -y

WORKDIR /app

COPY ./flag.txt .
COPY ./homelander .

EXPOSE 1337/tcp

CMD socat tcp-listen:1337,reuseaddr,fork EXEC:./tcache_chall