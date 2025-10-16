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


Requisitos Funcionais (o que o sistema faz)

O sistema deve permitir adicionar tarefas.

O sistema deve permitir listar todas as tarefas.

O sistema deve permitir atualizar o nome de uma tarefa existente.

O sistema deve permitir remover uma tarefa.

As tarefas devem ser mantidas enquanto o programa estiver em execução.

⚙️ Requisitos Não Funcionais (como o sistema se comporta)

O código deve ser escrito em Python 3.x.

O programa deve rodar em modo console (CLI).

O código deve ser modularizado (funções separadas).

O código deve ser validado automaticamente pelo GitHub Actions (CI).

O repositório deve seguir um fluxo organizado com Issues, Branches, e Commits descritivos.