import json
import os

ARQUIVO_TAREFAS = "tarefas.json"

def carregarTarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    return []

def salvarTarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8-sig") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

# --- CRUD atualizado com prioridade ---

def adicionar_tarefa(descricao, prioridade):
    tarefas = carregarTarefas()
    tarefas.append({"descricao": descricao, "concluida": False, "prioridade": prioridade})



    salvarTarefas(tarefas)
    print(f"Tarefa '{descricao}' adicionada com prioridade '{prioridade}'!")

def listar_tarefas():
    tarefas = carregarTarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    print("\n--- Lista de tarefas ---")
    for i, tarefa in enumerate(tarefas):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i+1}. [{status}] {tarefa['descricao']} (Prioridade: {tarefa['prioridade']})")

def removerTarefa(indice):
    tarefas = carregarTarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    if 0 <= indice < len(tarefas):
        removida = tarefas.pop(indice)
        salvarTarefas(tarefas)
        print(f"Tarefa '{removida['descricao']}' removida com sucesso.")
        listar_tarefas()
    else:
        print("Índice inválido.")

def editar_tarefa(indice, nova_descricao):
    tarefas = carregarTarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    if 0 <= indice < len(tarefas):
        antiga = tarefas[indice]["descricao"]
        tarefas[indice]["descricao"] = nova_descricao
        salvarTarefas(tarefas)
        print(f"Tarefa '{antiga}' foi atualizada para '{nova_descricao}'.")
    else:
        print("Índice inválido.")

def marcar_concluida(indice):
    tarefas = carregarTarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvarTarefas(tarefas)
        print(f"Tarefa '{tarefas[indice]['descricao']}' marcada como concluída.")
    else:
        print("Índice inválido.")

def editar_prioridade(indice, nova_prioridade):
    tarefas = carregarTarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    if 0 <= indice < len(tarefas):
        tarefas[indice]["prioridade"] = nova_prioridade
        salvarTarefas(tarefas)
        print(f"Tarefa '{tarefas[indice]['descricao']}' agora tem prioridade '{nova_prioridade}'.")
    else:
        print("Índice inválido.")
