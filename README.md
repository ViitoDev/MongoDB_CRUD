# MongoDB CRUD com Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)

Este repositório contém um conjunto de scripts em Python desenvolvidos para demonstrar as operações fundamentais de **CRUD** (Create, Read, Update, Delete) utilizando um banco de dados **MongoDB**.

O projeto simula um sistema de gerenciamento de posts de um blog, permitindo criar, ler, atualizar e deletar documentos dentro de uma coleção.

## 📂 Estrutura do Projeto

O projeto está dividido em quatro scripts principais, cada um responsável por uma operação do CRUD:

| Arquivo | Função | Descrição |
| :--- | :--- | :--- |
| `create.py` | **Create** | Conecta ao banco e insere um novo documento (post) com título, categoria, nível e autor. |
| `read.py` | **Read** | Consulta o banco de dados e exibe todos os documentos armazenados na coleção. |
| `update.py` | **Update** | Localiza um documento existente (ex: nível "Intermediary") e atualiza seus dados (para "Starter"). |
| `delete.py` | **Delete** | Remove documentos do banco de dados baseados em um filtro específico (ex: categoria "Backend"). |

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem de programação principal.
* **MongoDB**: Banco de dados NoSQL orientado a documentos.
* **PyMongo**: Driver oficial do MongoDB para Python, usado para realizar a conexão e manipulação dos dados.

## 🚀 Como Executar

### Pré-requisitos

1.  Ter o **Python** instalado na sua máquina.
2.  Ter o **MongoDB** instalado e rodando localmente (ou uma string de conexão para um cluster remoto).
3.  Instalar a biblioteca `pymongo`.

### Instalação

Abra o terminal e instale a dependência necessária:

```bash
pip install pymongo
