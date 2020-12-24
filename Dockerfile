# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# get NLTK
RUN python3 -m nltk.downloader punkt

# port
EXPOSE 5000

# command to run on container start
CMD [ "python", "./main.py" ] 

