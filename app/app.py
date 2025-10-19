# app/app.py
import time
import os

from tarefas import (adicionar_tarefa, listar_tarefas,
removerTarefa, editar_tarefa, marcar_concluida, editar_prioridade)

# --- Função auxiliar para cores ---
def cor (texto, cor_codigo):
    cores = {
        "vermelho": "\033[91m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "azul": "\033[94m",
        "magenta": "\033[95m",
        "ciano": "\033[96m",
        "reset": "\033[0m",
    }
    return f"{cores.get(cor_codigo, '')}{texto}{cores[cor_codigo]}"

# --- Função principal ---

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(cor("\n╔══════════════════════════════════════╗", "azul"))
        print(cor("║ SISTEMA DE GERENCIAMENTO DE TAREFAS  ║", "ciano"))
        print(cor("╚══════════════════════════════════════╝\n", "azul"))
        print(cor("1️⃣  Adicionar tarefa", "verde"))
        print(cor("2️⃣  Listar tarefas", "verde"))
        print(cor("3️⃣  Remover tarefa", "verde"))
        print(cor("4️⃣  Editar tarefa", "verde"))
        print(cor("5️⃣  Marcar tarefa como concluída", "verde"))
        print(cor("6️⃣  Editar prioridade da tarefa", "verde"))
        print(cor("7️⃣  Sair\n", "vermelho"))
        print(cor("─────────────────────────────────────────────", "azul"))


        opcao = int(input(cor("\nEscolha uma opção: ", "amarelo")))

        if opcao == 1:
            nome = input("Digite o nome do tarefa: ")
            print("Prioridades")
            print("1 - Baixa")
            print("2 - Media")
            print("3 - Alta")
            escolha = int(input("Selecione a prioridade: "))
            if escolha == 1:
                prioridade = "Baixa"
            elif escolha == 2:
                prioridade = "Media"
            elif escolha == 3:
                prioridade = "Alta"
            else:
                print("Opção invalida!")
            adicionar_tarefa(nome, prioridade)
            time.sleep(1)

        elif opcao == 2:
            listar_tarefas()
            input("\nPressione qualquer tecla para voltar ao menu...")

        elif opcao == 3:
            try:
                indice = int(input("Digite o numero da tarefa que deseja remover: ")) - 1
                removerTarefa(indice)
            except ValueError:
                print(cor("⚠️  Digite um número válido.", "vermelho"))
                time.sleep(1.5)
        elif opcao == 4:
            try:
                indice = int(input("Digite o numero da tarefa que deseja editar: ")) - 1
                nova = input("Digite o nome do tarefa: ")
                editar_tarefa(indice, nova)
            except ValueError:
                print(cor("⚠️  Digite um número válido.", "vermelho"))
                time.sleep(1.5)
        elif opcao == 5:
            try:
                indice = int(input("Digite o numero da tarefa: ")) - 1
                marcar_concluida(indice)
            except ValueError:
                print(cor("⚠️  Digite um número válido.", "vermelho"))
                time.sleep(1.5)
        elif opcao == 6:
            try:
                indice = int(input("Digite o numero da tarefa: ")) - 1
                nova = input("Digite a nova prioridade (Baixa, Média, Alta: ")
                editar_prioridade(indice, nova)
            except ValueError:
                print(cor("⚠️  Digite um número válido.", "vermelho"))
                time.sleep(1.5)
        elif opcao == 7:
            print(cor("\n🚪 Saindo do sistema... Até logo!", "magenta"))
            time.sleep(1)
            break
        else:
            print(cor("⚠️  Opção inválida! Tente novamente.", "vermelho"))
            time.sleep(1.5)

if __name__ == "__main__":
        main()
