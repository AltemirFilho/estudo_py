# Vamos entender agora as tuplas
# As tuplas são semelhantes às listas, mas são imutáveis
# Isso significa que, uma vez criadas, não podemos alterar seus elementos
# Vamos ver um exemplo

minha_tupla = (1, 2, 3)
print(minha_tupla)

# Tentando alterar um elemento da tupla
# Isso vai gerar um erro
minha_tupla[0] = 4 # TypeError: 'tuple' object does not support item assignment

# As tuplas são importantes para quando queremos ter valores que não devem ser alterados