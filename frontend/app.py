import streamlit as st
import json
import requests

# Define the base URL of your FastAPI server
BASE_URL = "http://backend:8000"

# Function to create a user
def criar_usuario(nome:str, senha:str):
    response = requests.post(f"{BASE_URL}/criar_usuario", json={"nome":nome,"senha":senha})
    return response.json()

# Function to authenticate a user with text for sentiment analysis
def predicao_autenticada(nome, senha, texto):
    headers = {"nome":nome,"senha":senha}
    data = {"texto":texto}
    response = requests.post(f"{BASE_URL}/predicao_autenticada", headers=headers, json=data)
    return response.json()

# Function to get user registered
def obter_usuarios():
    response = requests.get(f"{BASE_URL}/usuarios")
    return response.json()

# Function to get user texts
def obter_textos(nome, senha):
    response = requests.get(f"{BASE_URL}/textos", headers={"nome": nome, "senha": senha}.json())
    return response.json()

# Streamlit App
st.title("FastAPI and Streamlit Integration - Sentiment Analysis")

# Create User Section
st.header("Create User")
new_username = st.text_input("Enter username:")
new_password = st.text_input("Enter password:", type="password")
if st.button("Create User"):
    if new_username and new_password:
        result = criar_usuario(new_username, new_password)
        st.write(result)
        

# Authentication Text Section
st.header("Text Analysis")
username = st.text_input("Enter username:", key="username")
password = st.text_input("Enter password:", type="password", key="password")

# Allow the user to enter a text for sentiment analysis
text_to_analyze = st.text_area("Enter text for sentiment analysis:")

if st.button("Authenticate and Analyze Sentiment"):
    
    result = predicao_autenticada(username, password, text_to_analyze)
    st.write(result)
    
# List available users
st.header("List all users")
st.write("Get the list of all registered users")
if st.form("Get All Users"):
    result = obter_usuarios()
    st.write(result)
    
# Get User Texts Section
st.header("Get User Texts")
if st.checkbox("View User Texts"):
    if username and password:
        texts = obter_textos(username, password)
        if texts:
            st.table(texts)
        else:
            st.info("No texts available for this user.")
    else:
        st.error("You need to authenticate first to view texts.")
