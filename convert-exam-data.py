import pandas as pd
from unidecode import unidecode

# Função para remover acentos de uma string
def remove_accents(input_str):
    return unidecode(input_str)

# Carregar o arquivo Excel
df = pd.read_excel('exame-csv.xlsx')

# Remover acentos e concatenar as colunas com vírgula
df['Concatenado'] = df.apply(lambda row: ','.join([remove_accents(str(cell)) for cell in row]), axis=1)

# Salvar o resultado em um novo arquivo CSV com a codificação correta
df.to_csv('exame-unificado.csv', index=False, encoding='utf-8-sig')