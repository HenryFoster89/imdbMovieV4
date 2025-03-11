from utils.download_data_v2 import download_csv_from_imdb
from utils.db_connection import execute_sql_script

execute_sql_script("create_tables.sql")
download_csv_from_imdb()
execute_sql_script("bulk_insert.sql")