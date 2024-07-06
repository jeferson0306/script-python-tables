import pandas as pd
from unidecode import unidecode
from pymongo import MongoClient
import logging

# Configurando o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Função para remover acentos de uma string
def remove_accents(input_str):
    return unidecode(input_str)


try:
    # Conectar ao MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    logging.info("Conexão ao MongoDB estabelecida com sucesso.")
    db = client["exam_data"]
    collection = db["exams"]
    logging.info("Conexão com a coleção 'exams' estabelecida com sucesso.")

    # Carregar o arquivo Excel
    df = pd.read_excel('exame-csv.xlsx')
    logging.info("Arquivo Excel carregado com sucesso.")

    # Remover acentos e concatenar as colunas com vírgula
    df['Concatenado'] = df.apply(lambda row: ','.join([remove_accents(str(cell)) for cell in row]), axis=1)
    logging.info("Processamento de dados completado.")

    # Converter DataFrame para dicionário
    data_dict = df.to_dict("records")

    # Inserir dados na coleção do MongoDB
    if data_dict:
        insert_result = collection.insert_many(data_dict)
        if len(insert_result.inserted_ids) == len(data_dict):
            logging.info("Todos os dados foram inseridos com sucesso no MongoDB.")
        else:
            logging.error("Não todos os registros foram inseridos.")
    else:
        logging.warning("Nenhum dado para inserir no MongoDB.")

    # Salvar o resultado em um novo arquivo CSV com a codificação correta
    df.to_csv('exame-unificado.csv', index=False, encoding='utf-8-sig')
    logging.info("Arquivo CSV salvo com sucesso.")

except pd.errors.EmptyDataError:
    logging.error("O arquivo Excel está vazio.")
except pd.errors.ParserError:
    logging.error("Erro ao analisar o arquivo Excel.")
except Exception as e:
    logging.error("Erro inesperado: %s", e)
    raise
finally:
    # Fecha a conexão com o banco de dados
    client.close()
    logging.info("Conexão com o MongoDB fechada.")
