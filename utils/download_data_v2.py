import os
import json
import polars as pl
from pathlib import Path

from utils.utils import get_time
from utils.config import DATA_DIR, UTILS_DIR

SCRIPT_DIR = Path(__file__).parent                  # Ottieni la directory dove è salvato lo script (MA a cosa serve quì ?)
TABLE_JSON = os.path.join(UTILS_DIR, "table_url.json")
           

def download_csv_from_imdb():     
    
    with open(TABLE_JSON) as f:                         # TABLE_JSON è un dizionario con il seguente formato:    {tableName: tableUrl}               
        imdb_url = json.load(f)   

    for values in imdb_url.values():                                                                
                              
        get_time(message = f"Downloading and converting: {values}")
        
        dfPolars = pl.read_csv(values , separator="\t", quote_char = """""", null_values= ["\\N"])      # Legge il file, quote_char è il carattere che racchiude i valori, null_values sono i valori nulli
        
        filename = values.split("/")[-1].replace(".tsv.gz", "").replace(".", "_")                       # Ricava un fileName dal link, sostituendo i caratteri non validi
        dfPolars.write_csv(os.path.join(DATA_DIR, filename +".csv"))                                    # Salva il file in formato csv
            

    