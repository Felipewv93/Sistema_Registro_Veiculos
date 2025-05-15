import pandas as pd

dados_banco = pd.DataFrame([
    {'bnome': 'Banco Itaú S/A.', 'bendereco': ' Praça Alfredo Egydio de Souza Aranha, 100B, Jabaquara, São Paulo/SP', 'id_proprietario': ''},
    {'bnome': 'Banco do Brasil S.A. ', 'bendereco': 'Rua Quinze de Novembro, 111, Sé, São Paulo - SP', 'id_proprietario': ''},
    {'bnome': 'Banco Bradesco S.A.', 'bendereco': 'Av. Paulista, 52, Bela Vista, São Paulo/SP', 'id_proprietario': ''},
    {'bnome': 'Banco Santander (Brasil) S.A.', 'bendereco': 'Avenida Juscelino Kubitschek, 2235 e 2241, Vila Olímpia, São Paulo/SP', 'id_proprietario': ''},
    {'bnome': 'Caixa Econômica Federal', 'bendereco': 'Avenida Senador Queirós, 111, Centro, São Paulo/SP'}
])

dados_caminhao = pd.DataFrame([
    {'cod_veiculo': '12345678900', 'marca_caminhao': 'Volvo', 'modelo_caminhao': 'FH', 'capacidade_peso': 28000, 'ano_caminhao': 2021},
    {'cod_veiculo': '32165498701', 'marca_caminhao': 'Scania', 'modelo_caminhao': 'P8', 'capacidade_peso': 80000, 'ano_caminhao': 2023},
    {'cod_veiculo': '15952369780', 'marca_caminhao': 'Volkswagen', 'modelo_caminhao': 'Meteor 29-530', 'capacidade_peso': 63879, 'ano_caminhao': 2025},
    {'cod_veiculo': '31546582103', 'marca_caminhao': 'Ford', 'modelo_caminhao': 'c-1933-Tractor', 'capacidade_peso': 45150, 'ano_caminhao': 2020},
    {'cod_veiculo': '98765410323', 'marca_caminhao': 'Mercedes-Benz', 'modelo_caminhao': 'Actros 2553', 'capacidade_peso': 62000, 'ano_caminhao': 2022},
])

dados_carro = pd.DataFrame([
    {}
])

dados_dono = pd.DataFrame([
    {}
])

dados_empresa = pd.DataFrame([
    {}
])

dados_pessoa = pd.DataFrame([
    {}
])

dados_proprietario = pd.DataFrame([
    {}
])

dados_veiculo_registrado = pd.DataFrame([
    {}
])

with pd.ExcelWriter('dados.xlsx', engine='openpyxl') as writer:
    dados_banco.to_excel(writer, sheet_name='Banco', index=False)
    dados_caminhao.to_excel(writer, sheet_name='Caminhão', index=False)
    dados_carro.to_excel(writer, sheet_name='Carro', index=False)
    dados_dono.to_excel(writer, sheet_name='Dono', index=False)
    dados_empresa.to_excel(writer, sheet_name='Empresa', index=False)
    dados_pessoa.to_excel(writer, sheet_name='Pessoa', index=False)
    dados_proprietario.to_excel(writer, sheet_name='Proprietário', index=False)
    dados_veiculo_registrado.to_excel(writer, sheet_name='Veículo_Registrado', index=False)