# app/app.py
from tarefas import adicionar_tarefa, listar_tarefas

def main():
    # Teste simples para validar que tarefas.py funciona
    adicionar_tarefa("Testar CI")
    adicionar_tarefa("Criar README")
    listar_tarefas()

if __name__ == "__main__":
    main()
