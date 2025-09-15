# API de Usuários - FastAPI

Esta é uma API REST simples desenvolvida com FastAPI, SQLAlchemy e SQLite, que permite gerenciar usuários com operações CRUD básicas.

## 🚀 Tecnologias

- **FastAPI** - Framework web moderno e rápido para Python
- **Uvicorn** - Servidor ASGI para execução da aplicação
- **SQLAlchemy** - ORM para interação com banco de dados
- **Pydantic** - Validação e serialização de dados
- **SQLite** - Banco de dados leve e embarcado

## 📁 Estrutura do Projeto

```
📦 API
├── 📜 main.py           # Ponto de entrada da aplicação e rotas da API
├── 📜 models.py         # Modelos do banco de dados (SQLAlchemy)
├── 📜 database.py       # Configuração e conexão com o banco de dados
├── 📜 requirements.txt  # Dependências do projeto
├── 📜 users.db          # Banco de dados SQLite (gerado automaticamente)
└── 📜 README.md         # Documentação do projeto
```

## 🛠️ Instalação e Execução

### Pré-requisitos
- Python 3.7+
- pip (gerenciador de pacotes do Python)

### Passos para instalação

1. **Clone o repositório** (se aplicável)
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Execute a aplicação:**
   ```bash
   uvicorn main:app --reload
   ```
4. **Acesse a documentação interativa:**
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## 📸 Interface da API

<img width="1414" height="636" alt="image" src="https://github.com/user-attachments/assets/c82d26f7-edbf-4455-a294-0cca4c48f1c4" />

**Acesse a documentação interativa:** @http://127.0.0.1:8000/docs

## 📋 Endpoints da API

### Criar Usuário
- **POST** `/users`
- **Body:**
  ```json
  {
    "nome": "João Silva",
    "email": "joao@email.com"
  }
  ```

### Listar Usuários
- **GET** `/users`
- **Resposta:** Lista de todos os usuários cadastrados

### Deletar Usuário
- **DELETE** `/users/{user_id}`
- **Parâmetros:** `user_id` (ID do usuário a ser deletado)

## 🗄️ Modelo de Dados

### User
- `id` (Integer, Primary Key) - Identificador único
- `nome` (String) - Nome do usuário
- `email` (String, Unique) - Email único do usuário

## 🔧 Funcionalidades

- ✅ Criação de usuários
- ✅ Listagem de usuários
- ✅ Exclusão de usuários
- ✅ Validação de dados com Pydantic
- ✅ Banco de dados SQLite persistente
- ✅ Documentação automática com Swagger

## 📝 Notas

- O banco de dados SQLite (`users.db`) é criado automaticamente na primeira execução
- A API inclui validação automática de dados de entrada
- Documentação interativa disponível em `/docs` e `/redoc`
