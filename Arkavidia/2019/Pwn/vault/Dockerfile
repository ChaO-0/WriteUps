FROM ubuntu:latest

RUN apt update && \
    apt install socat lib32ncurses5 -y

WORKDIR /app

COPY ./flag.txt .
COPY ./vault .

RUN chmod 775 ./vault

CMD socat tcp-listen:8888,reuseaddr,fork EXEC:./vault,su=nobody