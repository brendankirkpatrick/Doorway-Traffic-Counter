# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

RUN pip install -U pip wheel cmake
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# Install the project dependencies
RUN pip install -r requirements.txt


# Copy the project files into the container
COPY . .

# Set the entry point for the container
CMD [ "python", "" ]