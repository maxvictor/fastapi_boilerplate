# 🚀 FastAPI Boilerplate

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green.svg)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/pydantic-2.0+-blue.svg)](https://docs.pydantic.dev/)
[![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-2.0+-orange.svg)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)
[![CI](https://github.com/maxvictor/fastapi_boilerplate/actions/workflows/test.yml/badge.svg)](https://github.com/maxvictor/fastapi_boilerplate/actions)

---

## 📦 Sobre o Projeto

Este é um **boilerplate em FastAPI** com estrutura modular, escalável e pronta para produção, seguindo boas práticas de Clean Architecture.

Ideal para construção de microsserviços modernos com suporte a:
- Retry e Circuit Breaker
- Validações com Pydantic
- Estrutura de controllers, services e gateways
- Logs estruturados (Datadog, CloudWatch, etc)
- Docker e testes automatizados com pytest
- Leitura de variáveis via `.env`

---

## 🧱 Estrutura

```sh
project_root/
├── app/
│   ├── core/                         # Configurações e utilitários globais
│   │   ├── config.py                # Variáveis de ambiente, constantes globais
│   │   ├── exceptions.py            # Exceções personalizadas
│   │   ├── logging_config.py        # Logs estruturados (Datadog, etc.)
│   │   └── response.py              # Formatação padrão de respostas
│   
│   ├── data/                         # Esquemas (DTOs) e entidades
│   │   ├── models/                  # Models de persistência (ORMs)
│   │   │   └── post_model.py
│   │   └── schemas/                 # Schemas de entrada/saída (Pydantic)
│   │       └── post_schema.py
│
│   ├── domain/                       # Regras de negócio (casos de uso)
│   │   └── post_service.py
│
│   ├── gateways/                     # Integrações externas (API, banco, cache...)
│   │   ├── external_api.py          # API externa com retry e circuit breaker
│   │   └── database.py              # Configuração do banco (SQLAlchemy)
│
│   
│   ├── presentation/                # Camada de apresentação (API HTTP)
│   │   ├── controllers/             # Controllers que lidam com lógica HTTP
│   │   │   └── post_controller.py
│   │   
│   │   ├── routers/                 # Agrupa e versiona as rotas
│   │   │   ├── v1/                  # Versão 1 da API
│   │   │   │   └── post_router.py
│   │   │   
│   │   │   └── api_router.py   # Une todas as versões da API
│
│   
│   └── main.py                   # Ponto de entrada do FastAPI
│
├── tests/                            # Testes automatizados (pytest, mock)
│   └── test_post.py
│
├── .dockerignore                     # Arquivos ignorados pelo docker
├── .env                              # Variáveis de ambiente
├── .flake8                           # Arquivo de configuração do flake8
├── .gitignore                        # Arquivos ignorados pelo git
├── docker-compose.yml                # (opcional) para banco/cache
├── Dockerfile                        # Dockerização da aplicação
├── Makefile                          # Scripts facilitadores
├── pytest.ini                        # Arquivo de configuração do pytest
├── README.md                         # Documentação do projeto
└── requirements.txt                  # Dependências
```
# Observações:
- Controllers separam a lógica de HTTP das rotas (boas práticas)
- Routers em `v1/`, `v2/` permitem versão de API
- Schemas ficam em `data/schemas` e models de banco em `data/models`
- Gateways podem ser chamados de clients, mas `gateway` é mais genérico
- Core centraliza tudo que pode ser reutilizado entre projetos
- Retry/circuit breaker ficam em `gateways/external_api.py`
- Os testes simulam tanto domínio quanto integração com routers/controllers

## 📅 Variáveis de Ambiente

Configure seu arquivo `.env` com base no exemplo do arquivo `.env-example`:

| Variável               | Descrição                                                  |
|------------------------|------------------------------------------------------------|
| `API_BASE_URL`         | URL base da API externa a ser consumida                    |
| `LOG_LEVEL`            | Nível de logging (`INFO`, `DEBUG`, `WARNING`, `ERROR`)     |
| `RETRY_ATTEMPTS`       | Quantidade de tentativas de retry para falhas externas     |
| `CIRCUIT_BREAKER_TIMEOUT` | Tempo de reset do circuit breaker (segundos)            |
| `ENVIRONMENT`          | Ambiente atual do projeto (`local`, `dev`, `prod`)         |
| `PYTHONPATH`           | Caminho raiz para importações relativas no VSCode          |

---


## 🚀 Como Rodar o Projeto

### 🔧 Pré-requisitos

- Python 3.11+
- [Poetry](https://python-poetry.org/) ou `pip`
- (opcional) Docker

### 📥 1. Clone o repositório

```bash
git clone https://github.com/maxvictor/fastapi-boilerplate.git
cd fastapi-boilerplate
```

### 🧪 2. Crie um ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
```

### 📦 3. Instale as dependências

```bash
pip install --upgrade pip
make install
# ou
pip install -r requirements.txt
```

### ⚙️ 4. Configure o arquivo .env

```bash
cp .env-example .env
```

Edite o `.env` com as informações corretas (ver tabela acima).

### ▶️ 5. Execute o projeto

```bash
make run
# ou
uvicorn app.main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs) 🚀

---

## 🧪 Rodar os testes

```bash
make test
# ou
pytest
```

---

## 🐳 Rodar com Docker

```bash
docker build -t fastapi-boilerplate .
docker run -p 8000:8000 fastapi-boilerplate
```

---

## 🧰 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [Tenacity](https://tenacity.readthedocs.io/en/latest/)
- [aiobreaker](https://pypi.org/project/aiobreaker/)
- [Docker](https://www.docker.com/)
- [Pytest](https://docs.pytest.org/)
