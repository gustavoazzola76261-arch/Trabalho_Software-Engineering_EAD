# tests/test_tasks.py
from app.tarefas import adicionar_tarefa, listar_tarefas, removerTarefa

def run_tests():
    print("\n=== Início dos testes ===\n")

    # Adiciona tarefas
    adicionar_tarefa("Tarefa 1")
    adicionar_tarefa("Tarefa 2")
    listar_tarefas()

    # Remove a primeira tarefa
    removerTarefa(0)
    listar_tarefas()

    print("\n=== Testes concluídos com sucesso ===\n")

if __name__ == "__main__":
    run_tests()
