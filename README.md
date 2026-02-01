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

## 🚀 Tecnologias Utilizadas
- Python
- FastAPI
- Uvicorn
- OpenAPI / Swagger
- Banco de dados em arquivo (`.xlsx`)

---

## ▶️ Como rodar o projeto localmente

### 1️⃣ Clonar o repositório

### 2️⃣ Criar o ambiente virtual (venv)

```
python -m venv venv
```

### 3️⃣ Ativar o ambiente virtual

Windowns>

```
venv\Scripts\activate
```

Linux>
```
source venv/bin/activate
```

### 4️⃣ Instalar as dependências

```
python -m pip install -r requirements.txt
```

### 5️⃣ Rodar a aplicação

```
uvicorn app.main:app --reload
```

### 6️⃣ Acessar a aplicação

API: http://127.0.0.1:8000
Swagger (documentação interativa): http://127.0.0.1:8000/docs