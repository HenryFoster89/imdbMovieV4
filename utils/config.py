import os

# Configurazione del database
DB_SERVER = "localhost"
DB_NAME = "IMDb_v2"
DB_DRIVER = "ODBC Driver 17 for SQL Server"
DB_TRUSTED_CONNECTION = "yes"

# Configurazione dei percorsi
BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, "data")
SQL_DIR = os.path.join(BASE_DIR, "sql")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
UTILS_DIR = os.path.join(BASE_DIR, "utils")


"""
BASE_DIR
---------------------------------------------------------------------------------------------------------------
__file__ è una variabile python che contiene il percorso del file corrente(proprio quello che viene eseguito)
os.path.abspath(__file__) restituisce il percorso assoluto del file corrente
os.path.dirname(os.path.abspath(__file__)) restituisce la cartella in cui si trova il file corrente

Se ho bene capito fa tutto sto casino per rendere dinamico il percorso del file, in modo che se lo sposto in un'altra cartella
non devo modificare il percorso in tutte le righe di codice in cui è presente.
Ma perchè non usare semplicemente os.getcwd() che restituisce la cartella corrente in cui si trova il file?

os.getcwd() restituisce la cartella da cui viene eseguito lo script, non necessariamente la cartella in cui si trova lo script !!!!!!!!!!

"""