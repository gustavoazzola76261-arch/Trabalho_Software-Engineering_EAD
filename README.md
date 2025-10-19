📘 README.md atualizado
# 📝 Sistema de Gerenciamento de Tarefas (Python)

Este é um projeto simples em **Python** para gerenciar tarefas (CRUD completo), 
criado como parte de um estudo de **Boas Práticas de Engenharia de Software** 
com **GitHub Projects** e **GitHub Actions (CI)**.

---

## ⚠️ Gestão de Mudanças / Alteração de Escopo

**Alteração:** Implementar campo de **prioridade** para cada tarefa (Baixa, Média ou Alta).  

**Justificativa:**  
- Permitir ao usuário organizar melhor suas tarefas  
- Facilitar futuras melhorias, como filtros ou relatórios por prioridade  
- Demonstrar prática de gestão de mudanças e evolução do projeto  

**Impacto esperado:**  
- Atualização do CRUD (`tarefas.py`) para suportar prioridade  
- Atualização do menu (`app.py`) para permitir definir e listar prioridade  
- Atualização dos testes (`test_tasks.py`) para validar prioridade

---

## 🚀 Funcionalidades Atuais

- Adicionar tarefas
- Listar tarefas
- Remover tarefas
- Editar tarefas
- Marcar tarefas como concluídas
- Interface simples via terminal (menu interativo)
- Armazenamento em arquivo `tarefas.json`
- Testes automatizados
- Integração contínua (CI) via **GitHub Actions**

---

## 🧱 Estrutura do Projeto



Trabalho_Software-Engineering_EAD/
│
├── app/
│ ├── app.py # Código principal com menu
│ └── tarefas.py # Funções do CRUD
│
├── tests/
│ └── test_tasks.py # Testes automatizados
│
├── .github/
│ └── workflows/
│ └── ci.yml # Configuração do CI
│
├── tarefas.json # Arquivo onde as tarefas são salvas
└── README.md


---

## ⚙️ Como Executar o Projeto Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/gustavoazzola76261-arch/Trabalho_Software-Engineering_EAD.git
   cd Trabalho_Software-Engineering_EAD


Execute o programa:

python app/app.py


Para rodar os testes automatizados:

python tests/test_tasks.py

🔄 Integração Contínua (CI)

O repositório usa GitHub Actions para:

Configurar o ambiente Python 3.x

Rodar os testes unitários automaticamente a cada push

Validar que o projeto está íntegro e funcionando

Se o CI passar ✅, o código está estável.

📈 Próximos Passos

Melhorar a interface do menu (cores, separadores)

Adicionar filtros ou relatórios de tarefas

Expandir cobertura de testes para novos cenários

💡 Autor: Gustavo Azzola
📅 Última atualização: Outubro/2025