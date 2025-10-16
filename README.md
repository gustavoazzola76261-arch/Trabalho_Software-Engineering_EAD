# 🧠 Gerenciador de Tarefas (Projeto Base)

Este repositório contém a implementação inicial de um **sistema simples de gerenciamento de tarefas em Python**,
criado para fins educacionais e demonstração de boas práticas de **Engenharia de Software**
utilizando **GitHub Projects** e **GitHub Actions (CI)**.

---

## 🚀 Funcionalidades Atuais

- Adicionar novas tarefas  
- Listar tarefas cadastradas  
- Remover tarefas existentes  
- Menu interativo no terminal  

> 🔧 O projeto ainda está em desenvolvimento e será expandido gradualmente (ex.: salvar tarefas em arquivo, atualizar tarefas, etc).

---

## 🧩 Estrutura do Projeto



Trabalho_Software-Engineering_EAD/
│
├── .github/
│ └── workflows/
│ └── ci.yml # Executa o app automaticamente via GitHub Actions
│
├── app/
│ ├── app.py # Arquivo principal com menu simples
│ └── tarefas.py # Funções de CRUD (adicionar, listar, remover)
│
└── README.md


---

## ⚙️ Como Executar Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/gustavoazzola76261-arch/Trabalho_Software-Engineering_EAD.git
   cd Trabalho_Software-Engineering_EAD


Execute o programa:

python app/app.py

🚦 Integração Contínua (CI)

O projeto utiliza o GitHub Actions para garantir que o código seja executado corretamente a cada push na branch main.

📈 Próximos Passos

 Implementar atualização de tarefas

 Adicionar persistência (salvar tarefas em arquivo JSON)

 Criar testes automatizados (Pytest)

 Melhorar interface e modularização

👨‍💻 Autor

Gustavo Azzola
📚 Projeto desenvolvido para estudos e práticas de Engenharia de Software.