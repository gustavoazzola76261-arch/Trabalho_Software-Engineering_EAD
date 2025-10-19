# app/tarefas.py
import json
import os

#caminho do arquivo onde as tarefas serão salvas
ARQUIVO_TAREFAS = "tarefas.json"
#Carrega as tarefas do arquivo
def carregarTarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding = "utf-8-sig") as f:
            return json.load(f)
    return []
#Salva as tarefas no aquivo
def salvarTarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding = "utf-8-sig") as f:
        json.dump(tarefas, f, ensure_ascii = False, indent = 4)

#Funções principais do CRUD

def adicionar_tarefa(descricao):
    tarefas = carregarTarefas()
    tarefas.append({"descricao" :descricao, "concluida" : False})
    salvarTarefas(tarefas)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def listar_tarefas():
    tarefas = carregarTarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    print("\n --- Lista de tarefas ---")
    for i, tarefas in enumerate(tarefas):
        status = "✅" if tarefas["concluida"] else "❌"
        print(f"{i+1}. [{status}] {tarefas['descricao']}")



def removerTarefa(indice):
    tarefas = carregarTarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    if 0 <= indice < len (tarefas):
        removida = tarefas.pop(indice)
        salvarTarefas(tarefas)
        print(f"Tarefa '{removida['descricao']}' removida com sucesso.")
        listar_tarefas() # atualiza a lista de tarefas

    else:

        print("Indice invalido")

def editar_tarefa(indice, nova_descricao):
    tarefas = carregarTarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    if 0 <= indice < len(tarefas):
        antiga = tarefas[indice]["descricao"]
        tarefas[indice]["descricao"] = nova_descricao
        salvarTarefas(tarefas)
        print(f"Tarefa '{antiga}' foi atualizada para '{nova_descricao}' com sucesso.")
    else:
        print("Indice invalido")

def marcar_concluida(indice):
    tarefas = carregarTarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvarTarefas(tarefas)
        print(f"Tarefa '{tarefas[indice]['descricao']}' marcada como concluida.")
    else:
        print("Indice invalido")