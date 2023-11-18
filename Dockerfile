# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app files to the container
COPY ./app ./

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port that the Flask app runs on
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the Flask application

CMD ["python","app.py"]