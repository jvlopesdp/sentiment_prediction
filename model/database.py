import sqlite3

PATH_DATABASE = "database.db"

def criar_conexao():
    """Create a connection to the database.

    Returns:
        conn: A SQLite database connection object.
        cursor: A cursor object for executing SQL queries.
    """
    conn = sqlite3.connect(PATH_DATABASE, check_same_thread=False)
    cursor = conn.cursor()
    return conn, cursor

def criar_tabelas(cursor):
    """Create database tables if they don't already exist.

    This function creates two tables:
    - 'textos': Stores information about texts, including 'id', 'nome', 'texto', and 'classificacao'.
    - 'usuarios': Stores information about users, including 'id', 'nome', and 'senha'.
    
    """
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS textos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            texto TEXT NOT NULL,
            classificacao TEXT NOT NULL,
            score FLOAT NOT NULL
        )
    """
    )
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    """
    )

def criar_base_de_dados():
    """Create the database and tables, and commit the changes.

    This function calls 'criar_tabelas' to create the necessary tables
    and commits the changes to the database.

    """
    conn, cursor = criar_conexao()
    criar_tabelas(cursor)
    conn.commit()
    conn.close()