# app/tarefas.py
tarefas = []  # Lista de tarefas

def adicionar_tarefa(nome):
    tarefas.append(nome)
    print(f"Tarefa '{nome}' adicionada ✅")

def listar_tarefas():
    if not tarefas:
        print("⚠️ Nenhuma tarefa cadastrada.")
    else:
        print("--- Lista de Tarefas ---")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
