import uvicorn
from fastapi import FastAPI, Header, HTTPException
from typing import List, Dict, Union
import sqlite3

from classes import Prediction, Texto, User
from database import criar_conexao, criar_base_de_dados
from sentiment_prediction import sentiment_analysis

# Create a FastAPI application
app = FastAPI()

@app.get("/")
def home():
    """Initial route of the API"""
    return {"message": "Welcome to the example API!"}

# API Routes

@app.post("/criar_usuario")
def criar_usuario(usuario: User):
    """Create a user and store their name and password in the database.

    Args:
        usuario (User): The user object containing 'nome' (username) and 'senha' (password).

    Returns:
        dict: A dictionary indicating the successful creation of the user.

    Raises:
        HTTPException: Raised if the user already exists.
    """
    conn, cursor = criar_conexao()
    try:
        cursor.execute(
            f"INSERT INTO usuarios (nome, senha) VALUES ('{usuario.nome}', '{usuario.senha}')"
        )
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="User already exists")
    finally:
        conn.commit()
    return {"mensagem": "User created successfully"}

@app.get("/usuarios", response_model=List[Dict[str, Union[int, str]]])
def obter_usuarios():
    """Retrieve registered users from the database.

    Returns:
        List: A list of dictionaries containing 'id' and 'nome' (username).

    Raises:
        HTTPException: Raised if there is an issue retrieving the users.
    """
    conn, cursor = criar_conexao()
    cursor.execute("SELECT id, nome FROM usuarios")
    usuarios = cursor.fetchall()
    usuarios = [{"id": usuario[0], "nome": usuario[1]} for usuario in usuarios]
    return usuarios

@app.post("/predicao_autenticada", response_model=Prediction)
def predicao(texto: Texto, nome: str = Header(None), senha: str = Header(None)):
    """Perform sentiment prediction with authentication.

    Args:
        texto (Texto): The text to be analyzed for sentiment.
        nome (str, optional): The username for authentication. Defaults to Header(None).
        senha (str, optional): The password for authentication. Defaults to Header(None).

    Returns:
        Prediction: A prediction object with 'predicao' and 'score'.

    Raises:
        HTTPException: Raised if authentication fails or there is an issue with sentiment analysis.
    """
    conn, cursor = criar_conexao()
    cursor.execute(f"SELECT * FROM usuarios WHERE nome = '{nome}' AND senha = '{senha}'")
    usuario = cursor.fetchone()
    if usuario is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    
    # Existing user
    predicao = sentiment_analysis(texto.texto)
    
    # Save prediction in the 'textos' table
    cursor.execute(
        f"INSERT INTO textos (nome, texto, classificacao, score) VALUES ('{nome}', '{texto.texto}', '{predicao['label']}', '{predicao['score']}')"
    )
    conn.commit()
    conn.close()
    return Prediction(predicao=predicao['label'], score=predicao['score'])

@app.get("/textos", response_model=List[Texto])
def get_textos(nome: str = Header(None), senha: str = Header(None)):
    """Retrieve texts for a specific user with authentication.

    Args:
        nome (str, optional): The username for authentication. Defaults to Header(None).
        senha (str, optional): The password for authentication. Defaults to Header(None).

    Returns:
        Textos: A list of texts objects containing 'id', 'nome', 'texto' and 'score'.

    Raises:
        HTTPException: Raised if authentication fails or there is an issue retrieving the texts.
    """
    conn, cursor = criar_conexao()
    cursor.execute(f"SELECT * FROM usuarios WHERE nome = '{nome}' AND senha = '{senha}'")
    usuario = cursor.fetchone()
    if usuario is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    
    # Retrieve all texts for that user
    cursor.execute(f"SELECT id, nome, texto, score FROM textos WHERE nome = '{nome}'")
    textos = cursor.fetchall()
    # Print the retrieved 'score' values for debugging
    for texto in textos:
        print("Score:", texto[3])
    textos = [Texto(id=texto[0], nome=texto[1], texto=texto[2], score = texto[3]) for texto in textos]
    return textos

if __name__ == "__main__":
    # Create the database and tables, and run the FastAPI application
    criar_base_de_dados()
    uvicorn.run(app, host="localhost", port=8000)