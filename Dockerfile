# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /home

# Copy the requirements file into the container
COPY requirements.txt .

# RUN pip install -U pip wheel cmake
# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# Install the project dependencies
# RUN pip install -r requirements.txt
RUN pip install --upgrade pip
RUN pip install cmake==3.25.2
RUN pip install dlib==19.24.1
RUN pip install argparse==1.4.0
RUN pip install schedule==1.1.0
RUN pip install numpy==1.24.3
RUN pip install scipy==1.10.1
RUN pip install imutils==0.5.4
RUN pip install opencv-python==4.5.5.64

# Copy the project files into the container
COPY . .

# Set the entry point for the container
CMD ["bash"]