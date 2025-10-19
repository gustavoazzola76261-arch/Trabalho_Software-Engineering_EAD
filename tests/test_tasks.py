# tests/test_tasks.py
import os
import sys
<<<<<<< HEAD

# Adiciona o caminho da pasta 'app' para importar tarefas.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.tarefas import carregarTarefas, salvarTarefas, adicionar_tarefa, removerTarefa, ARQUIVO_TAREFAS

def limpar_arquivo():
    """Remove o arquivo de tarefas antes de cada teste"""
=======
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.tarefas import carregarTarefas, salvarTarefas, adicionar_tarefa, removerTarefa, editar_tarefa, ARQUIVO_TAREFAS

def limpar_arquivo():
>>>>>>> 94c09c7 (Adição da opção de editar tarefas no menu)
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

<<<<<<< HEAD
=======
def test_editar_tarefa():
    limpar_arquivo()
    salvarTarefas(["Antiga tarefa"])
    editar_tarefa(0, "Nova tarefa")
    tarefas = carregarTarefas()
    assert "Nova tarefa" in tarefas
    assert "Antiga tarefa" not in tarefas
    print("✅ test_editar_tarefa passou")

>>>>>>> 94c09c7 (Adição da opção de editar tarefas no menu)
if __name__ == "__main__":
    print("\n=== Início dos testes simples de tarefas ===\n")
    test_adicionar_tarefa()
    test_remover_tarefa()
<<<<<<< HEAD
=======
    test_editar_tarefa()
>>>>>>> 94c09c7 (Adição da opção de editar tarefas no menu)
    print("\n=== Todos os testes passaram! ===\n")
