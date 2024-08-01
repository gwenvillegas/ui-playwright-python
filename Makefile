build:
	docker build -t ui-python -f Dockerfile .

test: 
	docker run --name ui-python-container --env-file .env ui-python:latest

clean:
	docker rm -f ui-python-container
	docker rmi ui-python