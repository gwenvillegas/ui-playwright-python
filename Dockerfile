FROM mcr.microsoft.com/playwright/python:v1.45.0-jammy
WORKDIR /usr/scr
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "pytest"]
