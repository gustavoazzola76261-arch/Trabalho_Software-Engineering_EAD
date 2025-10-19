🧠 Sistema de Gerenciamento de Tarefas (Python)

Projeto desenvolvido como parte de um estudo prático de Engenharia de Software, aplicando boas práticas, GitHub Projects (Kanban) e GitHub Actions (CI).
O sistema realiza um CRUD completo de tarefas, com interface de terminal aprimorada.

🚀 Funcionalidades Atuais

✅ Adicionar tarefas com prioridade (Baixa, Média, Alta)

✅ Listar tarefas com status e prioridade

✅ Remover tarefas

✅ Editar tarefas

✅ Marcar tarefas como concluídas

✅ Editar prioridade de tarefas

✅ Interface aprimorada com cores e separadores no terminal

✅ Armazenamento persistente em tarefas.json

✅ Testes automatizados com pytest

✅ Integração Contínua via GitHub Actions

🔄 Gestão de Mudanças (Simulação)
🧩 Mudança Solicitada:

Melhoria na interface do menu e adição de atributos extras nas tarefas (status e prioridade).
Ajustes no código, testes e documentação foram feitos para refletir essa evolução.

💡 Justificativa:

Durante a fase de testes e uso, identificou-se a necessidade de uma interface mais amigável e visualmente clara, facilitando a interação via terminal e tornando o sistema mais intuitivo.
Além disso, foi solicitado o controle de prioridade e status, ampliando o escopo inicial.

⚙️ Ações Realizadas:

Atualização do menu principal (app.py) com cores, ícones e separadores

Adição de campos prioridade e concluída em tarefas.py

Criação de novas funções:

editar_prioridade()

marcar_concluida()

Atualização dos testes (test_tasks.py) para cobrir novas funções

Atualização do README.md e adaptação do Kanban no GitHub Projects

🧱 Estrutura do Projeto
Trabalho_Software-Engineering_EAD/
│
├── app/
│   ├── app.py              # Menu principal com interface colorida
│   ├── tarefas.py          # Funções CRUD e controle de status/prioridade
│
├── tests/
│   └── test_tasks.py       # Testes automatizados
│
├── .github/
│   └── workflows/
│       └── ci.yml          # Integração contínua (executa testes)
│
├── tarefas.json            # Banco de dados local (gerado automaticamente)
│
└── README.md

🧪 Execução e Testes
▶️ Executar o sistema manualmente
python app/app.py

🧩 Executar os testes
python tests/test_tasks.py


Os testes validam automaticamente:

Adição, remoção e edição de tarefas

Marcação como concluída

Edição de prioridade

Persistência correta no arquivo JSON

⚙️ Integração Contínua (CI)

O GitHub Actions realiza automaticamente:

Configuração do ambiente Python 3.x

Execução do arquivo principal (app/app.py)

Rodagem dos testes unitários (test_tasks.py)

Validação da integridade do projeto a cada push

✅ Se todos os testes passam, o build é aprovado.
❌ Se algum falhar, o Action indica erro para revisão.

🗂️ Planejamento (Kanban no GitHub Projects)

Tarefas planejadas:

 Desenvolver programa principal

 Criar funções CRUD

 Implementar tratamento de erros

 Adicionar loop principal

 Criar feedbacks para o usuário

 Executar e testar programa

 Documentar (README e comentários)

 Criar testes unitários

 Aplicar CI

 Simular mudança de escopo (interface e prioridade)

📈 Próximos Passos

Adicionar opção de buscar tarefas por palavra-chave

Implementar filtro por prioridade ou status

Melhorar cobertura dos testes automatizados

👨‍💻 Autor

Gustavo Azzola
📅 Última atualização: Outubro/2025
📍 Projeto acadêmico — Engenharia de Software