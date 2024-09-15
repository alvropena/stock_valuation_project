# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry and dependencies
RUN pip install poetry
RUN poetry install

# Copy .env file
COPY .env /app/.env

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app using uvicorn server
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
