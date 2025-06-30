# Vamos aqui entender como fazer loops com (for...in)
# Primeiro precisamos entender que esse metodo gera um loop mais específico
# Ele percorre todos elementos de um coleção fazendo aquilo que o camando colocado por você pedir
# Vale colocar aqui de maneira mais clara ainda que ele fará o comando repetidamente em cada item da lista até sua condição de parada ser atendida


# Vamos criar uma lista parra o primeiro exemplo:
lista =  ['Python', 'SQL', 'Java', 'HTML', 'CSS']

for linguagem in lista: # A palavra "linguagem" é apenas uma variável temporaria que define cada passada por cada item da coleção 
    print(linguagem)