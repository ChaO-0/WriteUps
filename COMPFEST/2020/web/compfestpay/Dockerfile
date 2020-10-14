FROM ubuntu:20.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install build-essential -y
RUN apt-get install python python-dev python3-pip -y
RUN useradd --create-home --shell /bin/bash compfest12
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /home/compfest12/
COPY . /home/compfest12/
RUN chown -R compfest12:compfest12 .
RUN chmod 755 /home/compfest12/run.sh
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

USER compfest12

CMD ["/bin/sh", "/home/compfest12/run.sh"]
