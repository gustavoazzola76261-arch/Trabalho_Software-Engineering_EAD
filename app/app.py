# app/app.py
import time
from tarefas import removerTarefa

from tarefas import adicionar_tarefa, listar_tarefas

from tarefas import adicionar_tarefa, listar_tarefas, editar_tarefa


def main():
    while True:
        print ("\n===== MENU ====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Editar tarefa")
        print("5 - Sair")


        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            nome = input("Digite o nome do tarefa: ")
            adicionar_tarefa(nome)
        elif opcao == 2:
            listar_tarefas()
            time.sleep(1)

        elif opcao == 3:
            try:
                indice = int(input("Digite o numero da tarefa que deseja remover: ")) - 1
                removerTarefa(indice)
            except ValueError:
                print("Digite um numero valido")
        elif opcao == 4:
            try:
                indice = int(input("Digite o numero da tarefa que deseja editar: ")) - 1
                nova = input("Digite o nome do tarefa: ")
                editar_tarefa(indice, nova)
            except ValueError:
                print("Digite um numero valido")
        elif opcao == 5:
            print("Saindo do sistema...")
            break
        else:
            print("Opção invalida, tente novamente.")

if __name__ == "__main__":
        main()
