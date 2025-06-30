# Vamos juntar um pouco de tudo que foi visto nos materiais anteriores para criaramos uma lista de tarefas interativa


id_usuário = input("Olá, de quem irei gerenciar as tarefas hoje? ")
print(f"Perfeito {id_usuário.capitalize}, seja bem vindo ao seu gerenciador de tarefas!")
lista_tarefas = [] # Primeiro passo é criar uma lista vazia


while True: # Aqui quando definimos apenas (While True:) nos temos um motor  de funcionamente onde apenas parará nosso proggrama com o comando (break)
    print("\n--- Menu de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Ver Minhas Tarefas")
    print("4. Sair do programa")
# Definimos acima todas as opções que o o nosso usúario poderá ver e escolhar o que quer que o programa execute
# Agora vamos "dar vida" a essa funções definindo o que cada escolha fará para que o sistema execute
# Abaixo estão as definições, para facilitar farei em irdem do menu vizando a organização
# Vale lembrar que tudo tem de estar dentado corretamnete para que sempre esteja dentro do (while True:)

    selecao_menu = int(input("O que faremos agora? ")) # Altero a string para que ele sempre reconheça o valor de entrada como inteiro, medida de proteção contra bugs

    if selecao_menu == 1:
        nova_tarefa