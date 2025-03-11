# Import
import os
import gzip
import shutil
import requests
import json

from config import DATA_DIR, UTILS_DIR


"""
NECESSITA':
AL link https://datasets.imdbws.com/
    Sono presenti i file compressi XXXXX.tsv.gz
    Voglio scaricarli e convertili in .tsv

1) Download         XXXXX.tsv.gz
2) Conversione in   XXXXX.tsv 
    

"""


"""

probabilmente è meglio collegare un df direttamente al file online (probabilmente prima devo comunque decomprimerlo)
e fare un bulk insert direttamente.
passaggio successivo e fare un update delle sole celle aggiorante (come si fa?)

"""

# Variable / Constant
TABLE_JSON = os.path.join(UTILS_DIR, "table_url.json")

# Funzioni
#--------------------------------------------------------------------------#
def download_convert_files(tableName, tableUrl):
    """Downloads files from given URLs and saves them as .tsv.gz files."""
    
    os.makedirs(DATA_DIR, exist_ok=True)                        # Create directory if not exist    
    gz_path = os.path.join(DATA_DIR, tableName + ".tsv.gz")     # Percorso del file  .tsv.gz    (File scaricato e salvato)
    tsv_path = os.path.join(DATA_DIR, tableName + ".tsv")       # Percorso del file .tsv        (File aperto e decompresso)
    csv_path = os.path.join(DATA_DIR, tableName + ".csv")       # Percorso del file .csv        (File aperto e decompresso)
    response = requests.get(tableUrl, stream=True)              # Request url

    print(f"Downloading: {tableName}")
    # Apre un file binario in scrittura
    with open(gz_path, "wb") as file:                              # Crea/Apre tableName.tsv.gz
             for chunk in response.iter_content(chunk_size=1024):  # Scarica a blocchi di 1024 byte
                 file.write(chunk)                                 # Scrive su tableName.tsv.gz
                
    print(f"Downloaded: {tableName} \tSaved in {gz_path} \t as {tableName}.tsv.gz")
    
    with gzip.open(gz_path, 'rb') as f_in:
        with open(csv_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    print(f"Decompressed: {tableName}.tsv.gz in {tableName}.tsv")
    os.remove(gz_path)
    print(f"Deleted: {tableName}.tsv.gz")
    print("\n")



# Codice
#--------------------------------------------------------------------------#             

# Store dict. tableName : tableUrl             
with open(TABLE_JSON) as f:     
    """
    {tableName: tableUrl}
    """               
    imdb_url = json.load(f)     

# Download and Convert                            
for tableName, tableUrl in imdb_url.items():
    download_convert_files(tableName, tableUrl)

