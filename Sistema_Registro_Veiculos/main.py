# %%
# imports
import os

from dotenv import load_dotenv

from etl.etl import ETL

load_dotenv()

# %%
# conexão com o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")

# %%
# testando o ETL
origem = "dados2.xlsx"
#destino = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"
destino = f"mssql+pyodbc://localhost\\SQLEXPRESS/SRV2?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"


etl = ETL(origem, destino)

etl.extract()
etl.transform()
etl.load()
