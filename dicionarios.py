# Vamos agora começar a explorar a parte de dicionários, ferramanta que eleva nossas capacidades no python
# Entender e dominara a criação de dicionários é um ponta de partida impprtante para o estudo de dados


# Vamos criara e enrebder a melhor estrutura para criara nosso dicionário:
# Primeiro preciamos saber o diciooário é definidos por cahves {}


info_usuario = { # Perceba que abrimos o dicionário com as chaves, damos esse pulo de linha para organizar melhor o dicionário
    "nome": "Altemir", # Após definir a etiqueta que armazenará os dados, comolocar(:) e antes de passar para próxima categoria, finalizar com virgula para que o sistema entenda o fim da atual
    "idade": 24, # Podemos armazenar valores tambem
    "sexo": "Masculino",
    "estado civil": "casado",
    "interesses": ["programação", "jogos de computador", "cinema "], # Para adicionar mais de um item na categoria colocar no formato de lista
    "faz faculdade": True # Podemos armazenar volores booleanos tambem 
}


# Agora quee sabemos como criar um dicionnário, vamos entender como utilizar o mesmo


# Existem algumas maneiras de printar os valores de um dicionário, a mais comum é utilizando o nome da chave entre colchetes
print(info_usuario["nome"])  # Saída: Altemir
print(info_usuario["idade"])  # Saída: 24

# Podemos também utilizar o método get() para acessar os valores, que é mais seguro pois não gera erro se a chave não existir
print(info_usuario.get("sexo"))  # Saída: Masculino 
print(info_usuario.get("profissão", "Não especificada"))  # Saída: Não especificada (não gera erro), aqui podemos definir um valor padrão caso a chave não exista "não especificada"

# Para printar todas as chaves do dicionário, podemos usar o método keys()
print(info_usuario.keys())  # Saída: dict_keys(['nome', 'idade', 'sexo', 'estado civil', 'interesses', 'faz faculdade'])

# Para printar todos os valores do dicionário, podemos usar o método values()
print(info_usuario.values())  # Saída: dict_values(['Altemir', 24, 'Masculino', 'casado', ['programação', 'jogos de computador', 'cinema'], True])

# Para printar todos os itens (chave-valor) do dicionário, podemos usar o método items()
print(info_usuario.items())  # Saída: dict_items([('nome', 'Altemir'), ('idade', 24), ('sexo', 'Masculino'), ('estado civil', 'casado'), ('interesses', ['programação', 'jogos de computador', 'cinema']), ('faz faculdade', True)])

# Podemos printar o dicionário inteiro de uma vez
print(info_usuario)  # Saída: {'nome': 'Altemir', 'idade': 24, 'sexo': 'Masculino', 'estado civil': 'casado', 'interesses': ['programação', 'jogos de computador', 'cinema'], 'faz faculdade': True}

# Podemos printar o dicionário utilizando o metodo for
for chave, valor in info_usuario.items():
    print(f"{chave}: {valor}") # Verá que a saída será a mesma, mas com uma formatação diferente. Contendo cada informação em uma linha separada

# Podemos tambem verificar se uma chave ou valor existem no dicionário
print("nome" in info_usuario)  # Saída: True
print("profissão" in info_usuario)  # Saída: False  

# Verificando se um valor existe
print("Altemir" in info_usuario.values())  # Saída: True
