import os
import re
import time
import pyodbc
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from utils.utils import get_time
from utils.config import DB_SERVER, DB_NAME, DB_DRIVER, SQL_DIR

#============================================================================
#                               CONNECTION
#============================================================================

def get_connection_alchemy():    
    engine = create_engine(f"mssql+pyodbc://{DB_SERVER}/{DB_NAME}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server")         # Creazione dewll'engine
    return engine


#============================================================================
#                      READ SQL SCRIPT (from sql directory)
#============================================================================

def execute_sql_script(file_name):
    file_path = os.path.join(SQL_DIR, file_name)                    # Path del file SQL    
    engine = get_connection_alchemy()                               # Connessione al database

    with open(file_path, "r", encoding="utf-8") as file:            # Apertura del file SQL
        sql_script = file.read()                                    # Lettura del file SQL
        sql_script = re.sub(r'--.*?$', "", sql_script, flags=re.MULTILINE)                  # Rimuove i commenti SQL
        sql_statements = [stmt.strip() for stmt in sql_script.split(";") if stmt.strip()]   # Split ed eliminazione statement vuoti

    with engine.connect() as connection:
        transaction = connection.begin()                            # Avvia una transazione
        try:
            for sql_statement in sql_statements:
                get_time(f"{sql_statement.split("\n")[0]}")
                connection.execute(text(sql_statement))             # Usa text() per evitare errori
            transaction.commit()                                    # Conferma le modifiche
            get_time(f"{sql_statement.split("\n")[0]}eseguito con successo.")
        except SQLAlchemyError as e:
            transaction.rollback()                                  # Annulla in caso di errore
            print(f"Errore durante l'esecuzione dello script: {e}")

 
        












# Eseguire lo script

# Funzione per la connessione al database
def get_connection_pyodbc():
    try:
        conn = pyodbc.connect(
            f"DRIVER={{{DB_DRIVER}}};SERVER={DB_SERVER};DATABASE={DB_NAME};Trusted_Connection=yes"
            )
        print("Connessione al database riuscita!")
        return conn
    except pyodbc.Error as e:
        print(f"Errore durante la connessione al database: {e}")
        return None