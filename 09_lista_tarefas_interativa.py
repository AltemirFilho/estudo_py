# Vamos juntar um pouco de tudo que foi visto nos materiais anteriores para criaramos uma lista de tarefas interativa


id_usuário = input("Olá, de quem irei gerenciar as tarefas hoje? ")
print(f"Perfeito {id_usuário.capitalize()}, seja bem vindo ao seu gerenciador de tarefas!")
lista_tarefas = [] # Primeiro passo é criar uma lista vazia


while True: # Aqui quando definimos apenas (While True:) nos temos um motor  de funcionamente onde apenas parará nosso proggrama com o comando (break)
    print("\n--- Menu de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Ver Minhas Tarefas")
    print("4. Sair do programa\n")
# Definimos acima todas as opções que o o nosso usúario poderá ver e escolhar o que quer que o programa execute
# Agora vamos "dar vida" a essa funções definindo o que cada escolha fará para que o sistema execute
# Abaixo estão as definições, para facilitar farei em irdem do menu vizando a organização
# Vale lembrar que tudo tem de estar dentado corretamnete para que sempre esteja dentro do (while True:)

    selecao_menu = int(input("O que faremos agora? ")) # Altero a string para que ele sempre reconheça o valor de entrada como inteiro, medida de proteção contra bugs

    if selecao_menu == 1:
        nova_tarefa = input("Qual tarefa deseja adicionar a sua lista de tarefas? ")
        lista_tarefas.append(nova_tarefa)
        print(f"{nova_tarefa} agora é uma tarefa da sua lista")
    
    elif selecao_menu == 2:
        if not lista_tarefas: # Aqui uso o (if not) para verificar se a lista é falsa, uma lista fazia é uma lista falsa para python 
             print("Não há tarefas para remover, sua lista está vazia!")
        else:
            print("essas são as tarefas da sua lista:")
            for indice, tarefa in enumerate(lista_tarefas): # Faz com que enumeremos as tarefas (enumerate), somando um ao indice para ser um número real
             print(f'{indice + 1}- {tarefa}')
            try: # Aqui nos preparamos para um possível erro com (try)
                numero_para_remover = int(input("Qual o número da tarefa que será removida? ")) # Criamos a variável para que a entrada do usuário se torne um número inteiro
                indice_real = numero_para_remover - 1 # Aqui transformamos o valor inserido pelo usuário no real valor correspondente ao indice do item na lista
                if 1 <= numero_para_remover <= len(lista_tarefas): # Definimos aqui o raio dos números que o usuário pode colocar, variando entre 1 e o ultimo número existente na lista
                    tarefa_removida = lista_tarefas.pop(indice_real) # Aqui preenchemos uma nova variavél com o retorno do que foi rtirado da lista com o (.pop)
                    print(f"Tarefa '{tarefa_removida}' removida com sucesso!") # A variável preenchida é exibida para que o usuário tenha um retorno do que foi retirado
                else:
                    print("Número inválido! Não existe uma tarefa com este número.")
            except ValueError: # Aqui evitamos que o programa crash, onde ao ter um erro o terminal retorna uma mensagem para o usuário
                print("Entrada inválida. Por favor, digite um número.")

    elif selecao_menu == 3:
        for indice, tarefa in enumerate(lista_tarefas):
             print(f'{indice + 1}- {tarefa}')

    elif selecao_menu == 4:
        print("Obrigado por usar a Lista de Tarefas. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 4.")