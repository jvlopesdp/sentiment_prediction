# Sentiment Analysis Web App

## Overview

This project is a web application that combines the power of Natural Language Processing (NLP) with FastAPI for the backend, Streamlit for the frontend, and the HuggingFace Transformers library for sentiment analysis. The application allows users to create accounts, authenticate, and analyze the sentiment of text inputs. Docker is used to containerize the application, making it easy to deploy and manage.

## Features

- User account creation and authentication.
- Sentiment analysis of text inputs using a state-of-the-art NLP model.
- Displaying the sentiment label and score.
- Viewing and managing user-specific text entries.
- Dockerized setup for easy deployment and scalability.
- Justfile to invoke main commands.

## Project Structure

The project is structured as follows:

- **Backend (FastAPI):** The backend API responsible for user management and sentiment analysis.
- **Frontend (Streamlit):** The user interface for interacting with the application.
- **HuggingFace Transformers:** Utilized for sentiment analysis.
- **Docker:** Used for containerization and managing dependencies.
- **Database:** SQLite is used for user and text storage.

## Usage

To run the application, you can use Docker Compose. Make sure you have Docker installed on your system.

1. Clone the repository:
```
git clone https://github.com/jvlopesdp/sentiment_prediction.git
```

2. Navigate to the project directory:
3. Build and start the Docker containers:
```
just up or if you don't have just installed
docker-compose up --build
```
4. Access the web application in your browser at [http://localhost:8501](http://localhost:8501).

## Dependencies

- FastAPI
- Streamlit
- Transformers by HuggingFace
- Docker

# Points of Improvement

While this project is fully functional, there are several areas where improvements can be made:

- **Dependency Management:** Consider using a tool like Poetry for managing Python dependencies.
- **Container Orchestration:** Explore Kubernetes for more advanced container management and scaling.
- **Infrastructure as Code (IaC):** Use Terraform to manage the infrastructure on AWS for better scalability and maintainability.
- **User Experience:** Enhance the frontend to provide a more user-friendly interface and additional features.
- **Security:** Implement proper user authentication mechanisms and protect against security vulnerabilities.

## Next Steps

The next steps for this project include:

1. Setting up the infrastructure on AWS using Terraform.
2. Deploying the application to AWS.
3. Implementing automated testing and CI/CD pipelines.
4. Enhancing the user interface and adding more features.

Feel free to contribute or fork the project to customize it according to your needs.
