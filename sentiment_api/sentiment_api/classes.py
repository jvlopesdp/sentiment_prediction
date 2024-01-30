from pydantic import BaseModel

# Define data model for API response
class Prediction(BaseModel):
    """Data model for API response"""

    predicao: str  # A string representing the sentiment prediction
    score: float   # A floating-point value representing the score associated with the sentiment prediction

class Texto(BaseModel):
    """Data model for API input"""

    texto: str  # A string representing the input text to be analyzed for sentiment
    score: float  # A float representing the sentiment score associated with the text

class User(BaseModel):
    """Data model for API input with authentication"""
    nome: str    # A string representing the username
    senha: str   # A string representing the user's password