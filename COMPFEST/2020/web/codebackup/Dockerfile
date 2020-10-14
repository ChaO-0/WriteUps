# This is model Dockerfile only
FROM python:3.8-alpine3.11

RUN apk update && apk add --update alpine-sdk busybox-initscripts

RUN mkdir -p path/to/codebackup/uploads
WORKDIR path/to/codebackup

# Install modules requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Application files
COPY main.py ./
COPY lib ./
COPY template ./

# Sensitive files
COPY this_is_not_real_flag_name.txt /
COPY env.yml /somewhere/over/the/rainbow/path/for/env.yml
RUN chmod 444 /this_is_not_real_flag_name.txt /somewhere/over/the/rainbow/path/for/env.yml

# Just in case you wanna hijack my server
RUN adduser nonroot --disabled-password
USER nonroot

EXPOSE PORT_NUMBER

ENTRYPOINT [ "python3", "main.py" ]
