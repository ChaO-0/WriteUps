FROM ubuntu:latest

RUN apt update && \
    apt install socat -y

WORKDIR /app

COPY ./flag.txt .
COPY ./canary-rop64 .

EXPOSE 12345/tcp

CMD socat tcp-listen:12345,reuseaddr,fork EXEC:./canary-rop64 
