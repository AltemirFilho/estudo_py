# Aqui vamos destrinchar o uso de if e else

print("Vamos identificar se um número é impa ou par!")
nmr = int(input("Insira aqui seu número: "))


# (if) define o ponto inicial de uma condição.
# Após definido a condição deve-se colocar (:) no final do bloco.
# Para que seja feita a dentação e o bloco a baqixo seja executado, sendo que apenas será sexecutado se condição for atendida.

if nmr == 0:
    print("0 nem é par nem é impar, é um número neutro.")
    tentar_novamente = input("Gostaria de tentar novamente? (s/n)")
    if tentar_novamente == "s" or tentar_novamente == "S":
        nmr = int(input("Insira aqui seu número: "))
        if nmr == 0:
            print(") nem é par nem é impar.")
            tentar_novamente = input("Gostaria de tentar novamente? (s/n)")
            if tentar_novamente == "s" or tentar_novamente == "S":
                nmr = int(input("Insira aqui seu número: "))


# (elif) define uma continuidade após o if
# Ou seja usamos o (elif) tem a mesma função do if porem é utilizado para dar segmento do bloco if
# Usado para verificar outras condições em sequeência se a do bloco if não for atendida


elif nmr%2 == 0:
    print(f'O número {nmr} é par.')


# (else) mostra toda condição possivel diferente do if
# Ou seja o (else) fecha o bloco if
# Serve como um plano de contigência caso nenhuma condição dos blocos acima seja atingida

else:  
    print(f"O número {nmr} é impar")



