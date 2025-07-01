# Agora vamos aprender como utilizar a função (def)
# Basicamente essa função empacota um bloco de código e da um nome a ele, fazendo com que possamos chamar e executar aquele codigo sem precisar reeescreve-lo
# (def) vem então como um facilitador e organizador do código, deixando tudo mais limpo e claro


# Para exemplificar bem como o código muda, vamos refazer o código do arquivo anterior usando (def)

id_usuário = input("Olá, de quem irei gerenciar as tarefas hoje? ")
print(f"Perfeito {id_usuário.capitalize()}, seja bem vindo ao seu gerenciador de tarefas!")
lista_tarefas = []
selecao_menu = int(input("O que faremos agora? "))

def adicionar_tarefa():
    nova_tarefa = input("Qual tarefa deseja adicionar a sua lista de tarefas? ")
    lista_tarefas.append(nova_tarefa)
    print(f"{nova_tarefa} agora é uma tarefa da sua lista")

def remover_tarefas():
    if not lista_tarefas: 
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
