# Agora vamos aprender como utilizar a função (def)
# Basicamente essa função empacota um bloco de código e da um nome a ele, fazendo com que possamos chamar e executar aquele codigo sem precisar reeescreve-lo
# (def) vem então como um facilitador e organizador do código, deixando tudo mais limpo e claro


# Para exemplificar bem como o código muda, vamos refazer o código do arquivo anterior usando (def)

id_usuário = input("Olá, de quem irei gerenciar as tarefas hoje? ")
print(f"Perfeito {id_usuário.capitalize()}, seja bem vindo ao seu gerenciador de tarefas!")
lista_tarefas = []

def adicionar_tarefa():
    nova_tarefa = input("Qual tarefa deseja adicionar a sua lista de tarefas? ")
    lista_tarefas.append(nova_tarefa)
    print(f"{nova_tarefa} agora é uma tarefa da sua lista")

def remover_tarefas():
    if not lista_tarefas: 
             print("Não há tarefas para remover, sua lista está vazia!")
    else:
        print("essas são as tarefas da sua lista:")
        for indice, tarefa in enumerate(lista_tarefas):
         print(f'{indice + 1}- {tarefa}')
        try: 
            numero_para_remover = int(input("Qual o número da tarefa que será removida? "))
            indice_real = numero_para_remover - 1
            if 1 <= numero_para_remover <= len(lista_tarefas): 
                tarefa_removida = lista_tarefas.pop(indice_real)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!") 
            else:
                print("Número inválido! Não existe uma tarefa com este número.")
        except ValueError: 
            print("Entrada inválida. Por favor, digite um número.")

def ver_tarefas():
    for indice, tarefa in enumerate(lista_tarefas):
         print(f'{indice + 1}- {tarefa}')

def sair_do_programa():
    print("Obrigado por usar a Lista de Tarefas. Até mais!")

while True:
    print("\n--- Menu de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Ver Minhas Tarefas")
    print("4. Sair do programa\n")
    selecao_menu = int(input("O que faremos agora? "))

    if selecao_menu ==1:
        adicionar_tarefa()
    
    elif selecao_menu ==2:
        remover_tarefas()

    elif selecao_menu ==3:
        ver_tarefas()
    
    elif selecao_menu ==4:
        sair_do_programa()
        break

    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 4.")