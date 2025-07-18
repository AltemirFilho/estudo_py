# Vamos aqui aprender a criar e manipular listas 


# Primeiro passo, vamos criar uma lista 
# Precisamos entender que uma lista funciona como um pratileira que guarda mais de um valor, diferente de uma variável comum que guarda um
# Vale salientar que os itens dentro da lista são contabilizados iniciando em 0, logo o primeiro item é o item 0, o segundo 1 e assim por sequência


# Criamos aqui um lista, vale observar que usamos [] ou invés de ().
metas_de_carreira = ['Aprender python', 'Dominar a linguagem', 'Criar um repositório que ajude outros', 'Aprender a aplicar python na IA']
print(metas_de_carreira) # Colocamos dentro dos colchetes para que o python entenda que queremod imprimir a lista


# Agora vamos entender como "printar" a lista da maneira que quisermos
print(metas_de_carreira[0]) # adicionamos após o nome da lista o indice exato que queremos printar, aqui no caso o [0]
print(metas_de_carreira[1:3]) # assim definimos um intervalo que queremos ver a nossa lista, excluindo o ponto final que colocamos e printando apenasd o que há entre eles
print(metas_de_carreira[:2])   # assim definimos apenas um ponto de parada, excluindo esse poonto do ptint e inicianso do começo da lista 
print(metas_de_carreira[1:]) # asssim definimos um ponto de partida do print que mostrará dali até o fim da lista


# Vamos agora entender como modificar os elemenetos de uma lista
metas_de_carreira[1] = "Ter domínio da lingua" # aqui nós substituimos um item especifico da lista, sinalizado por seu indice, por algo novo
print(metas_de_carreira) 

# Vamos criar mais uma lista para o proximo exemplo
metas_novas = ["Aprender flutter", "Aprender SQL", "Criar Materias de estudo no Github",]
metas_de_carreira[1:2] = metas_novas # aqui nós substituimos uma fatia de uma lista por outra lista, adicionando a lista nova naquela fatia da lista que foi adicionada
print(metas_de_carreira)

# Vamos adiconar algo em uma lista nesse agora
metas_de_carreira.append("Conseguir bons cerficados") # (.append) adiciona um novo item na lista citada antes do comando
print(metas_de_carreira) # Observe que o item adicionado vai para o ultimo lugar da lista 

# Vamos agora dicionara algo em uma posição específica da lista
metas_de_carreira.insert(0, "Entender a logica da programação") # Aqui adicionamos um item na posição 0 com (.insert)
print(metas_de_carreira) # Observe que agora o novo item se encontra na posição que foi designada 

# Vamos criar mais uma lista para o proximo exemplo
metas_futuras = ["Dar aula de programação", "Conseguir uma bolsa CNPQ",]
metas_de_carreira.extend(metas_futuras) # Aqui adicionamos uma lista na lista escolhida com (.extend())
print(metas_de_carreira)

# Agora vamos ver como remover itens da lista
metas_de_carreira.remove("Dar aula de programação") # Aqui nós tiramos umm item escolhendo direto pelo elemento
print(metas_de_carreira)
del metas_de_carreira[4] # Aqui nós estamos deletando um arquivo específico baseado no índice
print(metas_de_carreira) 
metas_de_carreira.pop(5) # Aqui nós tambem deletamos um arquivo específico com base no índice tambem, porem devolve o item excluido 
print(metas_de_carreira)

# Vamos agora aprender a organizar e ordenar as listas
# Vou criar uma lista numérica para facilitar a visualização dos proximos pontos
lista_numeros = [4,79,3,12,45,457,1,25,35] # Perceba que os números não estão ordenados 
lista_numeros.sort() # aqui deixamos a lista em ordem crescente com (.sort())
print(lista_numeros) 
lista_numeros.sort(reverse=True) # aqui agora vamos deixar a lista em ordem decrescente ao adicionar o (reverse=True)
print(lista_numeros)
lista_numeros.reverse() # Aqui com o (.reverse()) nós invertemos a ordem dos itens da lista selecionada
print(lista_numeros) # Como a lista anteriormente foi colocda em ordem decrescente veja que agora alista esta em ordem crescente
metas_ordenadas = sorted(metas_de_carreira) # Aqui nós criamos uma nova lista onde teremos os elementeos da lista seleciona organizadas em maneira crescente sem alterar a lista original
print(metas_ordenadas)

# Vamos agora ver alguns outros comandos
print(len(metas_de_carreira)) # Aqui nós vemos com o comando (len()) a quantidade de itens presente na lista escolhida 
print(metas_de_carreira.index("Aprender SQL")) # Aqui ele me da o index da primeira ocorrência do elemento escolhido
print(metas_de_carreira.count("Aprender python")) # Conta a quantidade de vezes que o item escolhido aparece na lista
# Use (lista.copy()) para criar um cópia da lista
# Use (lista.clear()) para limpara os itens da lista selecionado