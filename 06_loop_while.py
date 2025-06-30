# (while) será a maneira mais limpa e organizada de criar um loop
# Ao digitar (while) inserir a condição e fechar com (:) o bloco de instruções em seguida será executado até que a condição seja falsa
# Dessa maneira se economiza linhas e tempo para criar loops eficientes



# Para demonstrar o loop vamos fazer um especie de jogo
# Importo random para que a maquina possa gerar valores aleatórios que serão usados em nosso jogo


import random 


id_usuario = input('Bem-vindo, qual o sue nome? ')
print(f'Ola {id_usuario.capitalize}, vamos jogar um jogo de advinhação.') # (.capitalize) deixa a primeira letra da string maiuscula 

jogar_novamente = 's' # defino aqui uma variavel de controle para iniciar o proximo loop em cima dessa variável


while jogar_novamente.lower() == 's': # crio um loop para possiblitar o usuário pode jogar novamente após acertar 
                                      # Uso o (.lower) para posteriormente transformar todo input em minúsculo, evitando erros de entrada por caixa alta 
    numero_secreto = random.randint(0, 100) # Esse comando faz com o python gere um número aleatório entre 0 e 100
# Vale a pena lembrar que o python lê as linhas em ordem, logo isso tem de estar na primeira linha, para que o número ja tenha sido gerado antes mesmo dos inputs
   
    palpite_jogador = 0 # defino outra variável de controle para iniciar o próximo loop baseado nela 

    while palpite_jogador != numero_secreto : # colo o (while)  a condição de q as variaveis que ja pre-estabeleci sejam diferentes (!=)
        palpite_jogador = int(input("Qual número estou pensando? (0-100) ")) 
        if palpite_jogador < numero_secreto :
            print(f"Que pena {id_usuario}, palpite muito baixo, tente um número maior!")
        elif palpite_jogador > numero_secreto :
            print(f"Que pena {id_usuario}, palpite muito alto, tente um número menor!")
        else:
            print(f"Parabêns {id_usuario}, Acertou em cheio!")
    jogar_novamente = input("Gostaria de jogar mais uma vez? (s/n)")
print(f"Tudo bem {id_usuario}, nos vemos na proxima!")
   