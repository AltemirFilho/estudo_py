# Vamos entender agora as tuplas
# As tuplas são semelhantes às listas, mas são imutáveis
# Isso significa que, uma vez criadas, não podemos alterar seus elementos
# Vamos ver um exemplo

minha_tupla = (1, 2, 3)
print(minha_tupla)

# Tentando alterar um elemento da tupla
# Isso vai gerar um erro
try:    
    minha_tupla[0] = 4 # TypeError: 'tuple' object does not support item assignment
except TypeError as e:
    print(f"Erro, os valores da tupla não podem ser alterados: {e}") # Aqui colocamos uma mensagem de erro para entender o que aconteceu

# As tuplas são importantes para quando queremos ter valores que não devem ser alterados

# Podemos tranformar listas em tuplas usando a função tuple()
lista_convidados = ['Altemir', 'Giu', 'Biel'] # Aqui temos uma lista de convidados que podem ser alterados
lista_convidados.append('Lili') # Adicionando um novo convidado
print(lista_convidados)
lista_convidados[3] = 'Isa' # Alterando o nome de um convidado
print(lista_convidados)

#Agora vamos transformar essa lista em uma tupla
tupla_convidados = tuple(lista_convidados)
print(tupla_convidados) # Observe que agora ele imprime as informações entre paranteses, indicando que é uma tupla

# As tuplas são úteis quando queremos garantir que os dados não serão alterados acidentalmente
# Vamos agora fazer o nosso usuário criar uma tupla com informções pessoais

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")
tupla_usuario = (nome, idade, cidade) # Criando uma tupla com as informações do usuário
print(f"Tupla do usuário: {tupla_usuario}") # Imprimindo a tupla do usuário

# Caso queiramos que o usuario tenha a opção de adicionar mais uma tupla e colocar essas em uma lista, podemos fazer o seguinte:
lista_usuarios = [] # Criando uma lista para armazenar as tuplas de usuários
adicionar_usuario = 's' # Variável de controle para adicionar novos usuários

while adicionar_usuario.lower() == 's':
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cidade = input("Digite sua cidade: ")
    tupla_usuario = (nome, idade, cidade) # Criando uma tupla com as informações do usuário
    lista_usuarios.append(tupla_usuario) # Adicionando a tupla à lista
    adicionar_usuario = input("Deseja adicionar outro usuário? (s/n): ")

print("Lista de usuários:")
for usuario in lista_usuarios:
    print(usuario)
# Aqui temos um exemplo de como criar uma lista de tuplas com informações de vários usuários
# Isso é útil para armazenar dados de forma organizada e imutável