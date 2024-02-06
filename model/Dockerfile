# Use the official Python image as the base image specifically Python 3.10
FROM python:3.10

# Set the working directory within the container to /app
WORKDIR /app

# Copy the contents of the "model" directory from your host machine to the /app directory in the container
COPY . /app

# Copy the "requirements.txt" file from your host machine to the /app directory in the container
COPY requirements.txt /app/requirements.txt

# Install Python dependencies listed in the "requirements.txt" file
RUN pip install -r requirements.txt

# Expose port 8000 to allow external access to the container on port 8000 a(fastAPI-Backend Container)
EXPOSE 8000

# Define the default command to run when the container is started
# This command starts the Uvicorn ASGI server to run your FastAPI application
# "--host localhost" specifies that the server should listen only on localhost
# "--port 8000" specifies the port on which the server should listen

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

## Steps to run the application with docker:

### Build the Docker Image
#### docker build -t my-fastapi-app .

### Run the Docker Container:
#### docker run -d -p 8000:8000 --name fast-api-container my-fastapi-app

