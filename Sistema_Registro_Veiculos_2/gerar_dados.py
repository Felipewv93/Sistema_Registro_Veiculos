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
    {'cod_carro': '12345678910', 'estilo': 'SUV',   'marca_carro': 'BMW',      'modelo_carro': 'X5',         'ano_carro': '2020'},
    {'cod_carro': '23452567891', 'estilo': 'SEDAN', 'marca_carro': 'MERCEDES', 'modelo_carro': 'CLASSE E',   'ano_carro': '2021'},
    {'cod_carro': '23245678990', 'estilo': 'HATCH', 'marca_carro': 'HYUNDAI',  'modelo_carro': 'HB20',       'ano_carro': '2015'},
    {'cod_carro': '99887766554', 'estilo': 'PICKUP','marca_carro': 'FORD',     'modelo_carro': 'RANGER',     'ano_carro': '2019'},
    {'cod_carro': '88776655443', 'estilo': 'CONVERSÍVEL', 'marca_carro': 'AUDI', 'modelo_carro': 'A5 CABRIO', 'ano_carro': '2022'},
])


dados_dono = pd.DataFrame([
    {'id_proprietario': '1', 'cod_veiculo': '12345678910', 'data_compra': '2020-03-15', 'alienado_ou_regular': 'REGULAR'},
    {'id_proprietario': '2', 'cod_veiculo': '32165498701', 'data_compra': '2021-07-22', 'alienado_ou_regular': 'ALIENADO'},
    {'id_proprietario': '3', 'cod_veiculo': '98765410323', 'data_compra': '2016-01-10', 'alienado_ou_regular': 'REGULAR'},
    {'id_proprietario': '4', 'cod_veiculo': '88776655443', 'data_compra': '2019-09-30', 'alienado_ou_regular': 'ALIENADO'},
    {'id_proprietario': '5', 'cod_veiculo': '15952369780', 'data_compra': '2022-05-05', 'alienado_ou_regular': 'REGULAR'},
])

dados_empresa = pd.DataFrame([
    {'enome': 'Tech Solutions S.A.', 'eendereco': 'Avenida das Nações, 1234, São Paulo/SP', 'id_proprietario': '1'},
    {'enome': 'Automóveis Brasil Ltda.', 'eendereco': 'Rua do Automóvel, 4321, São Paulo/SP', 'id_proprietario': '2'},
    {'enome': 'Construtora ABC', 'eendereco': 'Rua das Flores, 567, Rio de Janeiro/RJ', 'id_proprietario': '3'},
    {'enome': 'Logística Express', 'eendereco': 'Avenida Paulista, 1000, São Paulo/SP', 'id_proprietario': '4'},
    {'enome': 'Global Importações', 'eendereco': 'Rua do Comércio, 9876, Curitiba/PR', 'id_proprietario': '5'},
])


dados_pessoa = pd.DataFrame([
    {'cpf': '123.456.789-00', 'num_carteira_motorista': '123456789', 'nome': 'João Silva', 'endereco': 'Rua dos Três, 10, São Paulo/SP', 'id_proprietario': '1'},
    {'cpf': '987.654.321-00', 'num_carteira_motorista': '987654321', 'nome': 'Maria Oliveira', 'endereco': 'Avenida Central, 250, Rio de Janeiro/RJ', 'id_proprietario': '2'},
    {'cpf': '111.222.333-44', 'num_carteira_motorista': '112233445', 'nome': 'Carlos Pereira', 'endereco': 'Rua das Palmeiras, 45, Curitiba/PR', 'id_proprietario': '3'},
    {'cpf': '222.333.444-55', 'num_carteira_motorista': '223344556', 'nome': 'Fernanda Souza', 'endereco': 'Rua do Sol, 100, Belo Horizonte/MG', 'id_proprietario': '4'},
    {'cpf': '333.444.555-66', 'num_carteira_motorista': '334455667', 'nome': 'Lucas Costa', 'endereco': 'Avenida Brasil, 890, Salvador/BA', 'id_proprietario': '5'},
])

dados_proprietario = pd.DataFrame([
    {'id_proprietario': '10'},
    {'id_proprietario': '20'},
    {'id_proprietario': '30'},
    {'id_proprietario': '40'},
    {'id_proprietario': '50'},
])


dados_veiculo_registrado = pd.DataFrame([
    {'cod_veiculo': '12345678910', 'placa': 'ABC-1234'},
    {'cod_veiculo': '23452567891', 'placa': 'XYZ-5678'},
    {'cod_veiculo': '23245678990', 'placa': 'LMN-2345'},
    {'cod_veiculo': '99887766554', 'placa': 'JKL-8765'},
    {'cod_veiculo': '88776655443', 'placa': 'QRS-3456'}
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