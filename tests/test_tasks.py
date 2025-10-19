# tests/test_tasks.py

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.tarefas import (
    carregarTarefas, salvarTarefas, adicionar_tarefa, removerTarefa,
    editar_tarefa, marcar_concluida, editar_prioridade, ARQUIVO_TAREFAS
)

# --- Função auxiliar ---
def limpar_arquivo():
    if os.path.exists(ARQUIVO_TAREFAS):
        os.remove(ARQUIVO_TAREFAS)

# --- Testes ---
def test_adicionar_tarefa():
    limpar_arquivo()
    adicionar_tarefa("Tarefa de teste1", "Baixa")
    adicionar_tarefa("Tarefa de teste2","Alta")
    adicionar_tarefa("Tarefa de teste", "Média")
    tarefas = carregarTarefas()
    descricoes = [t["descricao"] for t in tarefas]
    assert "Tarefa de teste" in descricoes
    print("✅ test_adicionar_tarefa passou")

def test_remover_tarefa():
    limpar_arquivo()
    salvarTarefas([
        {"descricao": "Tarefa A", "concluida": False, "prioridade": "Média"},
        {"descricao": "Tarefa B", "concluida": False, "prioridade": "Média"}
    ])
    removerTarefa(0)
    tarefas = carregarTarefas()
    descricoes = [t["descricao"] for t in tarefas]
    assert "Tarefa A" not in descricoes
    assert "Tarefa B" in descricoes
    print("✅ test_remover_tarefa passou")

def test_editar_tarefa():
    limpar_arquivo()
    salvarTarefas([{"descricao": "Antiga tarefa", "concluida": False, "prioridade": "Média"}])
    editar_tarefa(0, "Nova tarefa")
    tarefas = carregarTarefas()
    descricoes = [t["descricao"] for t in tarefas]
    assert "Nova tarefa" in descricoes
    assert "Antiga tarefa" not in descricoes
    print("✅ test_editar_tarefa passou")

def test_marcar_concluida():
    limpar_arquivo()
    salvarTarefas([{"descricao": "Tarefa teste", "concluida": False, "prioridade": "Média"}])
    marcar_concluida(0)
    tarefas = carregarTarefas()
    assert tarefas[0]["concluida"] == True
    print("✅ test_marcar_concluida passou")

def test_editar_prioridade():
    limpar_arquivo()
    salvarTarefas([{"descricao": "Tarefa teste", "concluida": False, "prioridade": "Média"}])
    editar_prioridade(0, "Alta")
    tarefas = carregarTarefas()
    assert tarefas[0]["prioridade"] == "Alta"
    print("✅ test_editar_prioridade passou")

# --- Execução dos testes ---
if __name__ == "__main__":
    print("\n=== Início dos testes simples de tarefas ===\n")
    test_adicionar_tarefa()
    test_remover_tarefa()
    test_editar_tarefa()
    test_marcar_concluida()
    test_editar_prioridade()
    print("\n=== Todos os testes passaram! ===\n")
