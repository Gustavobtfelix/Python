# Use an official Python runtime as the base image
FROM python:3

# Install CUPS library and Python CUPS package
RUN apt-get update && apt-get install -y \
    cups libcups2-dev \
    && pip install pycups

# Copy your Python script into the container
COPY listPrintersLinux.py /app/listPrintersLinux.py

# Set the working directory
WORKDIR /app

# Run your Python script when the container starts
CMD ["python", "listPrintersLinux.py"]













