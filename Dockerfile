# Use the official Python 3.8 image as the base image
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /uniconnect-authentication

# Copy the requirements.txt into the container
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Specify the command to run on container start
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "--workers", "4", "--threads", "4", "--access-logfile", "-"]

