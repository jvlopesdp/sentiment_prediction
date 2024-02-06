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

# Expose port 8501 to allow external access to the container on port 8501 (Streamlit - Frontend Container )
EXPOSE 8501

ENTRYPOINT ["streamlit","run"]

CMD ["app.py"]

## Steps to run the application with docker:

### Build the Docker Image
#### docker build -t frontend-image .

### Run the Docker Container:
### docker run -d -p 8501:8501 --name frontend-container frontend-image

