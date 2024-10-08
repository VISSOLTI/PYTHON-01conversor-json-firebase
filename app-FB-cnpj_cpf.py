import json
import pandas as pd
import numpy as np

df = pd.read_excel("consulta.xlsx")

#REMOVER A COLUNA FICHA CADASTRO
df = df.drop(["FICHA CADASTRO"], axis=1)

# Remover . / - da coluna CNPJ/CPF

df['CNPJ/CPF'] = df['CNPJ/CPF'].str.replace('[./-]', '', regex=True)
df['CNPJ/CPF'] = df['CNPJ/CPF'].str.rstrip()

# Converter para lista de listas
lista_de_listas = df.values.tolist()

# Criando um DataFrame
df = pd.DataFrame(lista_de_listas, columns=['CNPJ/CPF', 'COD_CLIENTE', 'V1', 'V2', 'FICHA'])

# Definindo o CNPJ/CPF como índice
df.set_index('CNPJ/CPF', inplace=True)


# Transformando o DataFrame em um dicionário
dicionario = df.to_dict('index')


# Convertendo o dicionário para formato JSON
json_data = json.dumps(dicionario, indent=4)

# Função para converter NaN para uma string específica
def nan_to_string(val):
    if isinstance(val, float) and np.isnan(val):
        return "N/A"
    else:
        return val

# Aplicar a função a todos os valores do dicionário
for chave, valor in dicionario.items():
    for k, v in valor.items():
        dicionario[chave][k] = nan_to_string(v)

# Converter para JSON
json_data = json.dumps(dicionario, indent=4)

#print(json_data)

# Salvando em um arquivo (opcional)
with open('CONSULTA-COMERCIAL.json', 'w') as f:
      f.write(json_data)




#056.122.507/0001-72