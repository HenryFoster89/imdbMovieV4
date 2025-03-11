"""
qui ci mettiamo una specie di menu che lancia gli script

"""

import os
print("Scaricamento dati IMDb...")
os.system("python utils\download_data.py")
#print("Creazione delle tabelle...")
#os.system("python import_data.py")
#print("Progetto completato con successo!")
