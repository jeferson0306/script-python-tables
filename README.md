# Projeto de Busca de Exames

Este projeto consiste em scripts Python que permitem buscar códigos de exames em um arquivo CSV e retornar informações detalhadas sobre o exame correspondente. O resultado de cada busca é registrado em um arquivo de log.

## Pré-requisitos

Antes de começar, é necessário ter o Python instalado na sua máquina. Este projeto foi testado com Python 3.8 ou superior. Você também precisará do gerenciador de pacotes `pip` para instalar as dependências.

## Configuração do Ambiente

Recomenda-se usar um ambiente virtual para evitar conflitos de dependências com outros projetos Python. Para configurar e ativar um ambiente virtual, siga os passos abaixo:

```bash
# Instalar o módulo venv, se ainda não estiver instalado
python3 -m pip install --user virtualenv

# Criar o ambiente virtual
python3 -m venv env

# Ativar o ambiente virtual
source env/bin/activate  # No macOS e Linux
env\\Scripts\\activate  # No Windows