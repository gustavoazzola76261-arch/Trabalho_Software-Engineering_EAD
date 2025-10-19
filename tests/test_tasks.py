# tests/test_tasks.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.tarefas import carregarTarefas, salvarTarefas, adicionar_tarefa, removerTarefa, editar_tarefa, ARQUIVO_TAREFAS

def limpar_arquivo():
    if os.path.exists(ARQUIVO_TAREFAS):
        os.remove(ARQUIVO_TAREFAS)

def test_adicionar_tarefa():
    limpar_arquivo()
    adicionar_tarefa("Tarefa de teste")
    tarefas = carregarTarefas()
    assert "Tarefa de teste" in tarefas
    print("✅ test_adicionar_tarefa passou")

def test_remover_tarefa():
    limpar_arquivo()
    salvarTarefas(["Tarefa A", "Tarefa B"])
    removerTarefa(0)
    tarefas = carregarTarefas()
    assert "Tarefa A" not in tarefas
    assert "Tarefa B" in tarefas
    print("✅ test_remover_tarefa passou")

def test_editar_tarefa():
    limpar_arquivo()
    salvarTarefas(["Antiga tarefa"])
    editar_tarefa(0, "Nova tarefa")
    tarefas = carregarTarefas()
    assert "Nova tarefa" in tarefas
    assert "Antiga tarefa" not in tarefas
    print("✅ test_editar_tarefa passou")

if __name__ == "__main__":
    print("\n=== Início dos testes simples de tarefas ===\n")
    test_adicionar_tarefa()
    test_remover_tarefa()
    test_editar_tarefa()
    print("\n=== Todos os testes passaram! ===\n")
