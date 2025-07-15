import json

id_usuario = input("Olá, de quem irei gerenciar as tarefas hoje? ")
print(f"Perfeito {id_usuario.capitalize()}, seja bem-vindo ao seu gerenciador de tarefas!")
lista_tarefas = []

def adicionar_tarefa():
    nova_tarefa = input("Qual tarefa deseja adicionar à sua lista de tarefas? ")
    lista_tarefas.append(nova_tarefa)
    with open('tarefas.json', 'w') as arquivo:
        json.dump(lista_tarefas, arquivo, indent=4)
    print(f"{nova_tarefa} agora é uma tarefa da sua lista")

def remover_tarefas():
    if not lista_tarefas:
        print("Não há tarefas para remover, sua lista está vazia!")
    else:
        print("Essas são as tarefas da sua lista:")
        for indice, tarefa in enumerate(lista_tarefas):
            print(f'{indice + 1}- {tarefa}')
            try:
                numero_para_remover = int(input("Qual o número da tarefa que será removida? "))
                indice_real = numero_para_remover - 1
                if 1 <= numero_para_remover <= len(lista_tarefas):
                    tarefa_removida = lista_tarefas.pop(indice_real)
                    with open('tarefas.json', 'w') as arquivo:
                        json.dump(lista_tarefas, arquivo, indent=4)
                    print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
                else:
                    print("Número inválido! Não existe uma tarefa com este número.")
            except ValueError:
                print("Por favor, insira um número válido.")

def ver_tarefas():
    if not lista_tarefas:
        print("Sua lista de tarefas está vazia!")
    else:
        with open('tarefas.json', 'r') as arquivo:
            tarefas_salvas = json.load(arquivo)
            for tarefa in tarefas_salvas:
                print(f'- {tarefa}')

def sair_do_programa():
    print("Obrigado por usar a Lista de Tarefas. Até mais!")

while True:
    print("\nEscolha uma opção:")
    print("1- Adicionar tarefa")
    print("2- Remover tarefa")
    print("3- Ver tarefas")
    print("4- Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        remover_tarefas()
    elif opcao == "3":
        ver_tarefas()
    elif opcao == "4":
        sair_do_programa()
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
