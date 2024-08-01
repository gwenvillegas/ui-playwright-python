## Overview

A simple UI automation framework using pytest-playwright.

## Seeting local .env

- Update .env local variables

## Running locally using virtual env

- Create virtual env: `python3 -m venv .venv`
- Activate virtual env: `source .venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`
- Install playwright: `playwright install`
- Run test: `pytest -s -v`

## Running locally using docker

- Build an image: `make build`
- Run test: `make test`
- Clean docker image/container: `make clean`
