import json

lista_tarefas = []

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas(lista):
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)
    print("Sua lista de tarefas foi salva.")

def adicionar_tarefa(lista_de_tarefas):
    nova_tarefa = input("Qual tarefa deseja adicionar? ")
    lista_de_tarefas.append(nova_tarefa)
    salvar_tarefas(lista_de_tarefas) 

def remover_tarefas(lista_de_tarefas):
    if not lista_de_tarefas:
        print("Não há tarefas para remover.")
        return 
    ver_tarefas(lista_de_tarefas, com_cabecalho=False) 
    try:
        numero_para_remover = int(input("Qual o número da tarefa que será removida? "))
        indice_real = numero_para_remover - 1 
        if 0 <= indice_real < len(lista_de_tarefas):
            tarefa_removida = lista_de_tarefas.pop(indice_real)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
            salvar_tarefas(lista_de_tarefas) 
        else:
            print("Número inválido! Não existe uma tarefa com este número.")
    except ValueError:
        print("Por favor, insira um número válido.")

def ver_tarefas(lista_de_tarefas, com_cabecalho=True):
    if com_cabecalho:
        print("\n--- Suas Tarefas Atuais ---")
    
    if not lista_de_tarefas:
        print("Sua lista de tarefas está vazia!")
    else:
        for indice, tarefa in enumerate(lista_de_tarefas):
            print(f'{indice + 1}- {tarefa}')

def main():
    id_usuario = input("Olá, de quem irei gerenciar as tarefas hoje? ")
    print(f"Perfeito {id_usuario.capitalize()}, seja bem-vindo ao seu gerenciador de tarefas!")
    tarefas_atuais = carregar_tarefas()

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar | 2. Remover | 3. Ver | 4. Sair")
        
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            adicionar_tarefa(tarefas_atuais)
        elif opcao == "2":
            remover_tarefas(tarefas_atuais)
        elif opcao == "3":
            ver_tarefas(tarefas_atuais)
        elif opcao == "4":
            print("Obrigado por usar a Lista de Tarefas. Até mais!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
main()
