# 📦 API de Produtos — Teste Técnico

Este projeto foi desenvolvido **exclusivamente como parte de um teste técnico**.

Algumas decisões de implementação **não refletem boas práticas de um ambiente real de produção**, mas foram adotadas **intencionalmente** devido ao **contexto controlado**, com o único objetivo de **facilitar a avaliação técnica do código, das rotas e da organização do projeto**.

### ⚠️ Observações Importantes
- Rotas sensíveis foram mantidas **abertas**, sem autenticação.
- Existe uma rota para **download direto do banco de dados**, o que **não seria recomendado em um cenário real**.
- Essas escolhas foram feitas **apenas para fins de demonstração e avaliação**.

Em um ambiente real, essas funcionalidades seriam protegidas por:
- autenticação/autorização
- controle de acesso
- camadas adicionais de segurança

---

# 📋 Requisitos Funcionais do Sistema

Desenvolver uma aplicação capaz de consultar automaticamente o site **worten.pt**, extrair informações de produtos e disponibilizá-las por meio de uma **API REST**, permitindo gerenciamento completo dos dados e exportação em arquivo.

---

## 🔍 Coleta de Dados (Web Scraping)

O sistema deve consultar o site **https://www.worten.pt** para cada produto monitorado e extrair os seguintes dados:

- **Nome do produto**
- **Link do produto**
- **Menor preço encontrado**
- **Nome do vendedor (loja)** que oferece o menor preço

### Regras:
- A consulta deve buscar sempre o **menor preço disponível** no momento da extração.
- Caso existam múltiplos vendedores, apenas o vendedor com o menor preço deve ser considerado.
- Os dados extraídos devem ser armazenados localmente para uso pela API.

---

## 🚀 Tecnologias Utilizadas
- Python
- FastAPI
- Openpyxl
- Selenium
- Swagger
- Banco de dados em arquivo (`.xlsx`)

---

## ▶️ Como rodar o projeto localmente

### 1️⃣ Clonar o repositório

### 2️⃣ Criar o ambiente virtual (venv)

```
python -m venv venv
```

### 3️⃣ Ativar o ambiente virtual

Windows

```
venv\Scripts\activate
```

Linux
```
source venv/bin/activate
```

### 4️⃣ Instalar as dependências

```
python -m pip install -r requirements.txt
```

### 5️⃣ Rodar a aplicação

```
python -m uvicorn main:app --reload
```

### 6️⃣ Acessar a aplicação

API: http://127.0.0.1:8000

Swagger (documentação interativa): http://127.0.0.1:8000/docs


