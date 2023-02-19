# Importando :
# io = Ferramenta para Trabalhar com E/S ( Entrada / Saída)
# os : Usar recursos do S.O como ler ou gravar arquivos
# re : Módulo de Expressões Regulares
# find_packages da Biblioteca setuptools : Funções Específicas do path sem precisar digitar 'os.path' toda vez
# setup da Biblioteca setuptools : Definir e Configurar pacotes Python ( Empacotar )

import io
import os
import re
from os import path

from setuptools import find_packages
from setuptools import setup

# Define a variável "this_directory" para ser o diretório absoluto do arquivo de configuração setup.py
# path.dirname(__file__) = Função da Biblioteca padrão "os.path" do Python que retorna o nome do diretório do arquivo Python atual
# "__file__" = É um argumento / variável pré-definidade no Python que contém o caminho absoluto do arquivo Python em que está sendo executado
# Ao chamar path.dirname() com __file__ como argumento, a função retorna o nome do diretório em que o arquivo Python atual está localizado.
# Por exemplo, se o arquivo Python estiver localizado em /home/user/projeto/meuarquivo.py, path.dirname(__file__) retornará /home/user/projeto, que é o nome do diretório que contém o arquivo Python atual.
# A função path.abspath() é então usada para retornar o caminho absoluto do diretório, que pode ser usado para acessar arquivos em diretórios relacionados ao arquivo Python atual.

# Função "open()" é usada para abrir o arquivo README.md no mesmo diretóio, combinando o diretório atual com o nome do arquivo usando a função "join()" da biblioteca "os.path"

# O conteúdo do arquivo é lido com o método "read()" da variável f e atribuído a variável "long_description" que será usada como a descrição longa do pacote no PyPI ( Python Package Index ) quando o pacote for distribuído
# PyPI é a sigla para "Python Package Index". Trata-se de um repositório público de pacotes de software Python que podem ser instalados usando o gerenciador de pacotes pip.

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# setup() = Função do "setuptools" que permite definir as informações sobre o pacote e suas dependências.
# name: o nome do pacote.
# version: a versão atual do pacote.
# url: o URL do site oficial do pacote.
# license: a licença sob a qual o pacote é distribuído.
# author: o nome do autor do pacote.
# author_email: o endereço de e-mail do autor do pacote.
# description: uma descrição curta do pacote.
# long_description: uma descrição mais longa do pacote, geralmente em formato markdown.
# long_description_content_type: o tipo de conteúdo da descrição longa, que geralmente é "text/markdown".
# packages: uma lista de pacotes incluídos no pacote.
# install_requires: uma lista de pacotes Python necessários para que o pacote funcione corretamente.
# classifiers: uma lista de strings que descrevem o estado de desenvolvimento do pacote, sua compatibilidade com diferentes versões do Python e outros metadados.

# Ao definir esses argumentos dentro de setup(), é possível criar um pacote Python que pode ser facilmente instalado e distribuído usando o pip e outros gerenciadores de pacotes.

setup(
    name="mario-gpt",
    version="0.1.2",
    url="https://github.com/shyamsn97/mario-gpt",
    license='MIT',

    author="Shyam Sudhakaran",
    author_email="shyamsnair@protonmail.com",

    description="Generating Mario Levels with GPT2. Code for the paper: 'MarioGPT: Open-Ended Text2Level Generation through Large Language Models', https://arxiv.org/abs/2302.05981",

    long_description=long_description,
    long_description_content_type="text/markdown",

    include_package_data = True,

    packages=find_packages(exclude=('tests',)),

    install_requires=[
        'torch',
        'transformers',
        'scipy',
        'tqdm',
        'pillow',
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
