from abc import ABC, abstractmethod
import pandas as pd
from sqlalchemy import create_engine

class AbstractETL(ABC):
    def __init__(self, origem: str, destino: str):
        self.origem = origem
        self.destino = destino
        self._dados_extraidos = None
        self._dados_transformados = None

    @abstractmethod
    def extract(self, file_path):
        # Lê os dados a partir do caminho do arquivo (origem)
        dados_banco = pd.read_excel(file_path, sheet_name='Banco', engine='openpyxl')
        dados_caminhao = pd.read_excel(file_path, sheet_name='Caminhão', engine='openpyxl')
        dados_carro = pd.read_excel(file_path, sheet_name='Carro', engine='openpyxl')
        dados_dono = pd.read_excel(file_path, sheet_name='Dono', engine='openpyxl')
        dados_empresa = pd.read_excel(file_path, sheet_name='Empresa', engine='openpyxl')
        dados_pessoa = pd.read_excel(file_path, sheet_name='Pessoa', engine='openpyxl')
        dados_proprietario = pd.read_excel(file_path, sheet_name='Proprietário', engine='openpyxl')
        dados_veiculo_registrado = pd.read_excel(file_path, sheet_name='Veículo_Registrado', engine='openpyxl')
        
        return dados_banco, dados_caminhao, dados_carro, dados_dono, dados_empresa, dados_pessoa, dados_proprietario, dados_veiculo_registrado

    @abstractmethod
    def transform(self, dados_banco, dados_caminhao, dados_carro, dados_dono, dados_empresa, dados_pessoa, dados_proprietario, dados_veiculo_registrado):
        # TODO: transforma os dados extraídos em um formato mais adequado para inserção
        
        # Exemplo de transformação em dados_banco
        dados_banco['bendereco'] = dados_banco['bendereco'].str.strip()  # Remove espaços extras
        dados_banco['bnome'] = dados_banco['bnome'].str.upper()  # Converte para maiúsculas

        # Exemplo de transformação em dados_carro
        dados_carro['ano_carro'] = pd.to_datetime(dados_carro['ano_carro'], format='%Y')  # Converte a coluna 'ano_carro' para datetime
        dados_carro = dados_carro.dropna(subset=['cod_carro'])  # Remove linhas com 'cod_carro' nulo

        # Exemplo de transformação em dados_dono
        dados_dono['data_compra'] = pd.to_datetime(dados_dono['data_compra'], errors='coerce')  # Converte para datetime e trata erros

        # Exemplo de transformação em dados_proprietario
        dados_proprietario['id_proprietario'] = dados_proprietario['id_proprietario'].astype(int)  # Garante que seja inteiro

        # Exemplo de transformação em dados_pessoa
        dados_pessoa['cpf'] = dados_pessoa['cpf'].str.replace(r'\D', '', regex=True)  # Remove caracteres não numéricos do CPF
        dados_pessoa['num_carteira_motorista'] = dados_pessoa['num_carteira_motorista'].astype(str)  # Garante que seja string

        # Exemplo de transformação em dados_veiculo_registrado
        dados_veiculo_registrado['placa'] = dados_veiculo_registrado['placa'].str.upper()  # Converte as placas para maiúsculas
        
        return dados_banco, dados_caminhao, dados_carro, dados_dono, dados_empresa, dados_pessoa, dados_proprietario, dados_veiculo_registrado
    
    @abstractmethod
    def load(self, dados_banco, dados_caminhao, dados_carro, dados_dono, dados_empresa, dados_pessoa, dados_proprietario, dados_veiculo_registrado, destino):
        # Cria uma engine a partir do destino (ex: banco de dados) e insere os dados transformados
        engine = create_engine(destino)

        # Inserindo os dados nas tabelas correspondentes no banco de dados
        dados_banco.to_sql('banco', engine, if_exists='replace', index=False)  # Tabela 'banco'
        dados_caminhao.to_sql('caminhao', engine, if_exists='replace', index=False)  # Tabela 'caminhao'
        dados_carro.to_sql('carro', engine, if_exists='replace', index=False)  # Tabela 'carro'
        dados_dono.to_sql('dono', engine, if_exists='replace', index=False)  # Tabela 'dono'
        dados_empresa.to_sql('empresa', engine, if_exists='replace', index=False)  # Tabela 'empresa'
        dados_pessoa.to_sql('pessoa', engine, if_exists='replace', index=False)  # Tabela 'pessoa'
        dados_proprietario.to_sql('proprietario', engine, if_exists='replace', index=False)  # Tabela 'proprietario'
        dados_veiculo_registrado.to_sql('veiculo_registrado', engine, if_exists='replace', index=False)  # Tabela 'veiculo_registrado'

        print("Dados carregados com sucesso no banco de dados.")
