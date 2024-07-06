import logging
import pandas as pd

# Configurando logging
logging.basicConfig(filename='search_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Carregar o arquivo CSV
df = pd.read_csv('exame-unificado.csv', header=None, names=['Concatenado'])


# Função para buscar por código
def buscar_por_codigo(codigo):
    # Limpar o código de entrada
    codigo = codigo.strip()
    # Logar a ação de busca
    logging.info(f'Busca pelo código: {codigo}')

    # Procurar a linha que contém exatamente o código especificado
    resultado = df[df['Concatenado'].apply(lambda x: x.split(',')[0].strip() == codigo)]

    if not resultado.empty:
        # Obter os dados do resultado
        dados = resultado['Concatenado'].to_string(index=False).split(',')
        # Criar uma mensagem formatada
        mensagem_formatada = f'o código inserido {dados[0]} está relacionado ao exame {dados[1]} no valor de {dados[2]} reais.'
        # Logar o resultado encontrado
        logging.info(mensagem_formatada)
        return mensagem_formatada
    else:
        # Logar caso não encontre nada
        mensagem_nao_encontrado = f'Nenhum resultado encontrado para o código: {codigo}'
        logging.info(mensagem_nao_encontrado)
        return mensagem_nao_encontrado


# Exemplo de uso da função de busca
codigo_input = input("Digite o código para busca: ")
print(buscar_por_codigo(codigo_input))
