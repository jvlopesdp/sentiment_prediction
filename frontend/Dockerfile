# Use the official Python image as the base image specifically Python 3.10
FROM python:3.10

# Set the working directory within the container to /app
WORKDIR /app

# Copy the contents of the "frontend" directory from your host machine to the /app directory in the container
COPY . /app

# Copy the "requirements.txt" file from your host machine to the /app directory in the container
COPY requirements.txt /app/requirements.txt

# Install Python dependencies listed in the "requirements.txt" file
RUN pip install -r requirements.txt

# Expose port 8000 to allow external access to the container on port 8000 and 8501 (fastAPI and Streamlit respectively)
EXPOSE 8501

# Define the default command to run when the container is started
# This command starts the Uvicorn ASGI server to run your FastAPI application
# "--host localhost" specifies that the server should listen only on localhost

ENTRYPOINT ["streamlit","run"]

CMD ["app.py"]

## Steps to run the application with docker:

### Build the Docker Image
#### docker build -t frontend-image .

### Run the Docker Container:
### docker run -d -p 8501:8501 --name frontend-container frontend-image

