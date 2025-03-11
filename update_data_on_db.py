from utils.create_tables import create_tables
from utils.download_data_v2 import download_csv_from_imdb
from utils.db_connection import execute_sql_script, get_connection_alchemy

create_tables()
download_csv_from_imdb()
execute_sql_script("bulk_insert.sql")