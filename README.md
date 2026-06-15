# API Cartas Pokémon

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791.svg)
![Docker](https://img.shields.io/badge/Docker-compose-2496ED.svg)
![Pytest](https://img.shields.io/badge/Pytest-9.1-0A9EDC.svg)

Uma aplicação REST desenvolvida em FastAPI para o gerenciamento completo de cartas Pokémon. O projeto armazena os dados em um banco PostgreSQL conteinerizado e conta com uma suite completa de testes automatizados integrados a um banco de dados isolado.

---

## Estrutura do Projeto

pokemon-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py         
│   ├── database.py      
│   ├── models.py        
│   ├── schemas.py      
│   └── crud.py         
│
├── tests/
│   ├── conftest.py     
│   └── test_cartas.py   
│
├── Dockerfile           
├── docker-compose.yml  
├── requirements.txt
├── pytest.ini     
├── .env                
├── README.md
└── .gitignore

---

# Tecnologias e Ferramentas

- Python 3.12
- FastAPI (Framework web de alta performance)
- SQLAlchemy (ORM para mapeamento do banco)
- PostgreSQL 16 (Banco de dados relacional)
- Docker & Docker Compose (Conteinerização)
- Pytest (Framework de testes automatizados)

---

# Configuração e Instalação 

## 1.Clonar Repositório

git clone git@github.com:Rhennan-ALT/Trabalho_P2_Gerenciamento_Cards.git
cd Trabalho_P2_BackEnd

## 2.Configurar Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto com as credenciais de acesso ao banco

DATABASE_URL=postgresql://admin:admin@db:5432/pokemon_db

## 3.Executar com Docker Compose

Suba toda a aplicação junto com o banco de dados, execute:

docker-compose up --build

---

# Executando os Testes

Os testes automatizados utilizam Pytest e validam todas as operações CRUD da API.

## Executar todos os testes
pytest -v

## Executar testes com cobertura
pytest --cov=app

---






