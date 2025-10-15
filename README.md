# TechFlow Solutions - Sistema de Gerenciamento de Tarefas

Projeto didático demonstrando fluxo ágil no GitHub: CRUD de tarefas em Flask, testes com PyTest e CI com GitHub Actions.

## Execução (local)
1. Criar e ativar virtualenv
2. Instalar dependências: `pip install -r app/requirements.txt`
3. Rodar: `python app/app.py`

## Endpoints
- GET /tasks
- GET /tasks/<id>
- POST /tasks  (json: {"title":"...", "description":"..."})
- PUT /tasks/<id>
- DELETE /tasks/<id>
