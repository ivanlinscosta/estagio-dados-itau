# Projeto de estágio em dados Itaú
## candidato
- Andreas Hukuhara Christe
- andreash.christe@hotmail.com
- CPF: 443.853.418-69

### Introdução
O projeto consiste em analisar o dataset Ecommerce disponível no kaggle (https://www.kaggle.com/datasets/raziehghahartars/ecommerce?resource=download) e responder o desafio proposto, assim como as 4 perguntas levantadas.

A análise completa e as respostas às questões estão no arquivo PDF na raiz do projeto.

### Linguagem e Bibliotecas utilizadas
- Python
- virtualenv
- pandas
- matplotlib
- seaborn
- numpy
- scipy
- scikit-learn

### como rodar:
1- Caso não tenha as bibliotecas instaladas no computador siga as seguintes orientações:
- pip install virtualenv   (caso não tenha instalado)
- entrar na pasta raiz do projeto
- virtualenv venv     (criar um ambiente python)
- Set-ExecutionPolicy Unrestricted -Force (Caso o ambiente Windows não permita ativar a virtualenv)
- .\venv\Scripts\activate   (ativar venv)
- .\venv\Scripts\pip3 install -r .\requirements.txt
- python -m ipykernel install --user --name=venv (para jupyter identificar o kernel venv)
- jupyter notebook
- Abrir o arquivo ipynb e selecionar o kernel venv

2 - Caso tenha instalado todas as bibliotecas:
- Abrir o terminal na raiz do projeto
- jupyter notebook
- Abrir o arquivo ipynb
