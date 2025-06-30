# Vamos aqui entender como fazer loops com (for...in)
# Primeiro precisamos entender que esse metodo gera um loop mais específico
# Ele percorre todos elementos de uma coleção, fazendo aquilo que o camando colocado por você pedir
# Vale colocar aqui de maneira mais clara ainda que ele fará o comando repetidamente em cada item da lista até sua condição de parada ser atendida


# Vamos criar uma lista parra o primeiro exemplo:
lista =  ['Python', 'SQL', 'Java', 'HTML', 'CSS']

for linguagem in lista: # A palavra "linguagem" é apenas uma variável temporaria que define cada passada por cada item da coleção 
    print(linguagem)

# Vamos definir uma variável para o próximo exemplo:
gato = 'amora'

for letra in gato: # Deixo esse exemplo so deixa explicito que o (for) passa por cada item de uma coleção
    print(letra) 

# Vamos criar duas variáveis para o proximo exemplo
numeros = [4,6,7,14,2]
soma = 0

for numero in numeros:
    soma += numero # Aqui colocamos os numeros da lista para se somar entre e serem acrecentados na variável soma.
    print(soma) # Lembre de printar para ver o resultado

# Vamos gerar uma sequência de números
for i in range(5): # Vale lembrar que a sequência inicia do zero
    print(i)

# Vamos aninhar uma função (for) dentro de outra
for i in range(4):
    for j in range(2):
        print(f"({i},{j})")

# Vamos criar outra lista para o próximo exemplo, onde podemos obter tanto o indice quanto o valor do elemento
frutas = ["banana", "Maça", "Morango"]

for indice, fruta in enumerate(frutas): # Aqui defino dois nomes distintos para cada item, ou seja posso colocar agora dois comandos em um mesmo item para serem feitos em uma mesma volta
    print(f"Ordem na lista: {indice}; Fruta: {fruta}") # O (enumerate) aqui me entrega o indice de cada coisa ou seja a posição 

# Vamos agora agrupar listas com informações
# para isso vamos criar 3 listas distintas
nomes = ['Altemir', 'Mari', 'Isa', 'Leo']
idades = [24, 18, 18, 18]
estado_civil = ['Casado', 'Namorando', 'Solteira', 'Namorando']

for nome, idade, estado in zip(nomes, idades, estado_civil): # Colocamos aqui tudo que nos queremos agrupar com o o for, agrupamento feito pelo comando (zip)
    print(f"{nome.capitalize()} tem {idade} anos e está {estado.lower()}!")

# Vamos agora mesclar o loop com (for) com o (if), aninhando assim uma função na outra
for i in range(21):
    if i % 2 == 0:
        print(i)
print("Todos esses números são pares e estão contidos entre 0 e 20")

# Colocando (for) para preencher uma lista
quadrados = [i**2 for i in range(6)] # Nesse nos definimos uma variável elevada ao quadradro (1**2) e depois definos um espaço de reptições a serem feitas (range(6))
print(f"Aqui estão os números de 0 a 5 elevados ao quadrado: {quadrados}")

# Agora vamos entender como quebramos um loop antes mesmo dele ser concluído
for i in range(4500):
    if i > 3: # Aqui nos definimos um condicional parq qunao i passe de número 3
        break # E aqui definimos a consequência, que seria esssa a quebra do loop
    print(i)

# Agora vamos entender como fazer com que uma função não acontece durante o loop
Idades = [14,45,22,12,16,36,12,17,18] 
for idade in Idades:
    if idade < 18:
        continue # perceba que como a condição (continue) esta ligada ao (if) quando a condição é atendida ele pula ela no loop
    print(idade) # Fazendo assim que apenas a idade que n atenda a condição (if) entre no loop
