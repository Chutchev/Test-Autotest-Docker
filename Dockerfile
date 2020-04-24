FROM python:3.8
WORKDIR /behave/cerber-ui

COPY requirements.txt /behave/cerber-ui
RUN pip3 install -r requirements.txt
COPY ./cerber-ui /behave/cerber-ui/
