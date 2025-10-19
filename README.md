# 📝 Sistema de Gerenciamento de Tarefas (Python)

Este é um projeto simples em **Python** para gerenciar tarefas (CRUD básico), 
criado como parte de um estudo de **Boas Práticas de Engenharia de Software** 
com **GitHub Projects** e **GitHub Actions (CI)**.

---

## 🚀 Funcionalidades Atuais

- Adicionar tarefas
- Listar tarefas
- Remover tarefas
- Interface simples via terminal (menu interativo)
- Armazenamento em arquivo `tarefas.json`
- Testes automatizados com **pytest**
- Integração contínua (CI) via **GitHub Actions**

---

<<<<<<< HEAD
=======
## ⚙️ Funcionalidades

- **Adicionar tarefa**  
- **Listar tarefas**  
- **Remover tarefa**  
- **Editar tarefa** ← nova funcionalidade adicionada
- **Interface simples via terminal (menu interativo)**
- **Armazenamento em arquivo** `tarefas.json`  
- **Integração contínua (CI)** via **GitHub Actions**

---

>>>>>>> 94c09c7 (Adição da opção de editar tarefas no menu)
## 🧱 Estrutura do Projeto

Trabalho_Software-Engineering_EAD/
│
├── app/
│ ├── app.py # Código principal com menu
│ ├── tarefas.py # Funções do CRUD
│
├── tests/
│ └── test_tasks.py # Testes automatizados
│
├── .github/
│ └── workflows/
│ └── ci.yml # Configuração do CI (executa testes no push)
│
└── README.md

<<<<<<< HEAD
yaml
Copiar código

=======
>>>>>>> 94c09c7 (Adição da opção de editar tarefas no menu)
---

## ⚙️ Como Executar o Projeto Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/gustavoazzola76261-arch/Trabalho_Software-Engineering_EAD.git
   cd Trabalho_Software-Engineering_EAD
Execute o programa:

bash
<<<<<<< HEAD
Copiar código
python app/app.py
Para rodar os testes:

bash
Copiar código
=======
python app/app.py

Para rodar os testes:

bash
>>>>>>> 94c09c7 (Adição da opção de editar tarefas no menu)
pytest tests/test_tasks.py
🔄 Integração Contínua (CI)
O repositório usa GitHub Actions para:

Configurar ambiente Python 3.x

Executar o script principal (app/app.py)

Rodar os testes unitários (pytest)

Validar que o projeto está íntegro a cada push

Se o CI passar ✅, o código está estável.

📈 Próximos Passos
Adicionar campo de status de conclusão nas tarefas (pendente/concluída)

Melhorar cobertura de testes


💡 Autor: Gustavo Azzola
📅 Última atualização: Outubro/2025