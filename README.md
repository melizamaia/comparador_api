# Comparador de Preços API

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi&logoColor=white)](#)
[![MIT](https://img.shields.io/badge/License-MIT-green.svg)](#licença)

API em **FastAPI** para comparar preços entre marketplaces (ex.: Amazon e Mercado Livre), com **autenticação por token** via header `Token`.

- **Health:** `GET /`
- **Comparar:** `GET /api/comparar?query=<termo>`  
  **Header obrigatório:** `Token: <API_KEY>`

---

## 1) Requisitos
- Python **3.11+**
- Git, curl
- **VS Code** com extensão **Python**
- **Linux/WSL:** `pyenv` (recomendado)  
- **Windows:** `venv` (nativo do Python)

---

## 2) Ambientes por SO

### 🔹 Linux / WSL (Debian/Ubuntu) — pyenv
> Se já tem o pyenv configurado, pule para “Instalar dependências”.

**Instalar pyenv rapidamente:**
```
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
exec "$SHELL"
```

Criar e ativar o ambiente do projeto:

```
pyenv install 3.11.9
pyenv virtualenv 3.11.9 comparador_api
pyenv activate comparador_api           # ativa na sessão atual
pyenv local comparador_api             # ativa automaticamente neste diretório
python -V
```

Alternativa Linux com venv nativo:

```
python -m venv .venv
source .venv/bin/activate
```

🔹 Windows (PowerShell) — venv
powershell

# dentro da pasta do projeto
```
python -m venv .venv
```

# se bloquear execução de script, libere na sessão atual:
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
```

# ativar
```
.\.venv\Scripts\Activate.ps1
```

# conferir
```
python -V
```
Alternativa Windows com pyenv-win (opcional): pyenv install 3.11.9 → pyenv virtualenv 3.11.9 comparador_api → pyenv activate comparador_api.

## 3) Instalar dependências
```
pip install -r requirements.txt
```
requirements.txt (sugerido):

```
fastapi>=0.115.0
uvicorn[standard]>=0.30.0
pydantic>=2.8.0
python-dotenv>=1.0.1
httpx>=0.27.0
pytest>=8.2.0
pytest-asyncio>=0.23.0
```

## 4) Variáveis de ambiente
Crie .env na raiz do projeto:

Linux/WSL
```
printf "API_KEY=meu_token_super_secreto\n" > .env
```
Windows (PowerShell)

```
"API_KEY=meu_token_super_secreto" | Out-File -Encoding ascii .env
```

## 5) Executar
```
uvicorn app.main:app --reload --env-file .env
```
# Swagger: http://127.0.0.1:8000/docs
# Health:  http://127.0.0.1:8000/

## 6) Testar
Swagger (Authorize)
Abra http://127.0.0.1:8000/docs

Clique Authorize → em Token, cole apenas o valor do API_KEY (sem “Token:”).

Authorize → Close → teste GET / e GET /api/comparar?query=notebook.

Linux/WSL
```
export API=http://127.0.0.1:8000
export TOKEN=meu_token_super_secreto
curl -i "$API/"
curl -i -H "Token: $TOKEN" "$API/api/comparar?query=notebook"
```

Windows (PowerShell)

```
$API   = "http://127.0.0.1:8000"
$TOKEN = "meu_token_super_secreto"
curl.exe -i "$API/"
curl.exe -i -H "Token: $TOKEN" "$API/api/comparar?query=notebook"
```

## 7) Estrutura

```
- app/
  - api/
    - comparador_routes.py
  - auth/
    - auth_handler.py
  - providers/
    - amazon_api.py
    - mercadolivre_api.py
  - services/
    - comparador_service.py
  - models/
    - produto_models.py
  - schemas/
    - produto_schema.py
- main.py
```

## 8) Troubleshooting (rápido)
403 Token inválido/ausente: o valor do header Token deve ser idêntico ao API_KEY do .env.

500 API_KEY não configurada: rode com --env-file .env na raiz do projeto.

422: query vazia ou com menos de 2 caracteres.

Porta 8000 ocupada:

Linux/WSL: fuser -k 8000/tcp

Windows: netstat -ano | findstr :8000 → taskkill /PID <PID> /F

## 9) MIT — veja LICENSE.
