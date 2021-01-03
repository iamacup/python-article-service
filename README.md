## What

This is a simple web service that takes some HTML and tries to get article data from it

post data in the form {"html": "some html data"} to the service, remember to include `Content-Type` heade set to `application/json`

## How (docker-compose)

`docker-compose -f docker-compose.yaml up --build`

## How (docker)

* `docker build -t myimage .`
* `docker run -p 5000:5000 myimage`

