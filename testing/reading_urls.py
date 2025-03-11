"""
Non so quale sia il metodo più corretto / veloce per importare i dati da https://datasets.imdbws.com/ al DB

1) Chatgpt mi ha consigliato quello che troviamo su download_data.py: Scaricare i file e salvarli. Mi sembra complesso e lento
2) Scaricare con Pandas e sparare su DB con .to_sql . mi pare che to_sql sia lento e suscettibile di problemi
3) BULK insert, dovrebbe essere il metodo più corretto da un punbto di vista di DB (e chi lo dice?). 
    abbiamo bisogno di un csv (temporaneo), a questo punto lo gestirei con polars che è più veloce di pandas ( Vedi testing_download)

"""
import os
import pandas as pd
import polars as pl
from pathlib import Path
from datetime import datetime

# Ottieni la directory dove è salvato lo script
SCRIPT_DIR = Path(__file__).parent


URL = "https://datasets.imdbws.com/title.ratings.tsv.gz"

def testing_download():   
    
    # PANDAS
    start = datetime.now()
    dfPandas = pd.read_csv(URL, sep = "\t" )
    end = datetime.now()
    elapsed_time = end - start
    print(f"PANDAS:\tTempo impiegato: {elapsed_time.total_seconds():.6f} secondi")
    
    # POLARS
    start = datetime.now()    
    dfPolars = pl.read_csv(URL , separator="\t", quote_char = """""")
    end = datetime.now()
    elapsed_time = end - start
    print(f"POLARS:\tTempo impiegato: {elapsed_time.total_seconds():.6f} secondi")     
    
    return dfPandas, dfPolars

def testing_download_save_csv():   
    
    # PANDAS
    start = datetime.now()
    dfPandas = pd.read_csv(URL, sep = "\t" )
    dfPandas.to_csv(os.path.join(SCRIPT_DIR,r"temp\pandas.csv"))
    end = datetime.now()
    elapsed_time = end - start
    print(f"PANDAS:\tTempo impiegato: {elapsed_time.total_seconds():.6f} secondi")
    
    # POLARS
    start = datetime.now()    
    dfPolars = pl.read_csv(URL , separator="\t", quote_char = """""")
    dfPolars.write_csv(os.path.join(SCRIPT_DIR,r"temp\polars.csv"))
    end = datetime.now()
    elapsed_time = end - start
    print(f"POLARS:\tTempo impiegato: {elapsed_time.total_seconds():.6f} secondi") 
    
    #return dfPandas, dfPolars

testing_download_save_csv()