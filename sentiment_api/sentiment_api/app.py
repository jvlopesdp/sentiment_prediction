import streamlit as st
import json
import requests

# Define the base URL of your FastAPI server
BASE_URL = "http://localhost:8000"

# Function to create a user
def criar_usuario(nome, senha):
    response = requests.post(f"{BASE_URL}/criar_usuario", json={"nome": nome, "senha": senha})
    return response.json()

# Function to authenticate a user
def autenticar_usuario(nome, senha):
    response = requests.post(f"{BASE_URL}/predicao_autenticada", headers={"nome": nome, "senha": senha}, json={"texto": "Sample Text"})
    return response.json()

# Function to get user texts
def obter_textos(nome, senha):
    response = requests.get(f"{BASE_URL}/textos", headers={"nome": nome, "senha": senha})
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
        st.success(result.get("mensagem", "User created successfully"))
    else:
        st.error("Both username and password are required.")

# Authentication Section
st.header("Authentication")
username = st.text_input("Enter username:")
password = st.text_input("Enter password:", type="password")
if st.button("Authenticate"):
    if username and password:
        result = autenticar_usuario(username, password)
        if "predicao" in result:
            st.success(f"Authentication successful. Sentiment Prediction: {result['predicao']} (Score: {result['score']})")
        else:
            st.error("Authentication failed.")
    else:
        st.error("Both username and password are required.")

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
