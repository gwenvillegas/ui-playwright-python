FROM mcr.microsoft.com/playwright/python:v1.45.0-jammy
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "pytest", "-s", "-v" ]