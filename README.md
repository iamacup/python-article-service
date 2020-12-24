## What

This is a simple web service that takes some HTML and tries to get article data from it

## How

* `docker build -t myimage .`
* `docker run -p 5000:5000 myimage`

post data in the form {"html": "some html data"} to the service, remember to include `Content-Type` heade set to `application/json`