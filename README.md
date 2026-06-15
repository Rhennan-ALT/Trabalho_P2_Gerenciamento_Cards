# API Cartas Pokémon

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791.svg)
![Docker](https://img.shields.io/badge/Docker-compose-2496ED.svg)
![Pytest](https://img.shields.io/badge/Pytest-9.1-0A9EDC.svg)

Uma aplicação REST desenvolvida em FastAPI para o gerenciamento completo de cartas Pokémon. O projeto armazena os dados em um banco PostgreSQL conteinerizado e conta com uma suite completa de testes automatizados integrados a um banco de dados isolado.

---

# Estrutura do Projeto
```text
pokemon-api/
│
├── app/
│   ├── __init__.py      # Inicializador do pacote Python do app
│   ├── main.py          # Ponto de entrada da API e definição das rotas
│   ├── database.py      # Configuração do SQLAlchemy e conexão com o banco
│   ├── models.py        # Modelos de tabela do banco de dados (SQLAlchemy)
│   ├── schemas.py       # Validação de dados e serialização (Pydantic)
│   └── crud.py          # Operações de persistência de dados (Create, Read, Update, Delete)
│
├── tests/
│   ├── conftest.py      # Fixtures do Pytest e banco de testes isolado
│   └── test_cartas.py   # Testes automatizados das rotas CRUD
│
├── Dockerfile           # Instalações e ambiente da imagem do app
├── docker-compose.yml   # Orquestração do app e dos bancos Postgres
├── requirements.txt     # Dependências do projeto (FastAPI, SQLAlchemy, etc.)
├── pytest.ini          # Arquivo de configuração do Pytest
├── .env                 # Variáveis de ambiente com dados sensíveis
├── README.md            # Documentação do projeto
└── .gitignore           # Arquivos e pastas ignorados pelo Git
```

---

# Tecnologias e Ferramentas
```bash
- Python 3.12
- FastAPI (Framework web de alta performance)
- SQLAlchemy (ORM para mapeamento do banco)
- PostgreSQL 16 (Banco de dados relacional)
- Docker & Docker Compose (Conteinerização)
- Pytest (Framework de testes automatizados)
```

---

# Configuração e Instalação 

## 1.Clonar Repositório
```bash
git clone git@github.com:Rhennan-ALT/Trabalho_P2_Gerenciamento_Cards.git
```
```bash
cd Trabalho_P2_BackEnd
```

## 2.Configurar Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto com as credenciais de acesso ao banco:
```bash
DATABASE_URL=postgresql://admin:admin@db:5432/pokemon_db
```

## 3.Executar com Docker Compose

Suba toda a aplicação junto com o banco de dados, execute:
```bash
docker-compose up --build
```

---

# Executando os Testes

Os testes automatizados utilizam Pytest e validam todas as operações CRUD da API.

## Executar todos os testes
```bash
pytest -v
```

## Executar testes com cobertura
```bash
pytest --cov=app
```

---






