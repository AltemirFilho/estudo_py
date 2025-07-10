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

# Verificando com if
if "idade" in info_usuario:
    print(f"A idade do usuário é: {info_usuario['idade']}")  # Saída: A idade do usuário é: 24  
else:
    print("A chave 'idade' não existe no dicionário.") # Saída: A chave 'idade' não existe no dicionário.

# Podemos adicionar novos itens ao dicionário
info_usuario["profissão"] = "Desenvolvedor"  # Adicionando uma nova chave-valor
print(info_usuario)  # Saída: {'nome': 'Altemir', 'idade': 24, 'sexo': 'Masculino', 'estado civil': 'casado', 'interesses': ['programação', 'jogos de computador', 'cinema'], 'faz faculdade': True, 'profissão': 'Desenvolvedor'}

# Podemos atualizar valores existentes
info_usuario["idade"] = 25  # Atualizando o valor da chave 'idade', saída: {'nome': 'Altemir', 'idade': 25, 'sexo': 'Masculino', 'estado civil': 'casado', 'interesses': ['programação', 'jogos de computador', 'cinema'], 'faz faculdade': True, 'profissão': 'Desenvolvedor'}

# Podemos remover itens do dicionário usando o método pop()
info_usuario.pop("sexo")  # Remove a chave 'sexo' e retorna seu valor
print(info_usuario)  # Saída: {'nome': 'Altemir', 'idade': 25, 'estado civil': 'casado', 'interesses': ['programação', 'jogos de computador', 'cinema'], 'faz faculdade': True, 'profissão': 'Desenvolvedor'}

# Podemos remover um item usando o método del
del info_usuario["estado civil"]  # Remove a chave 'estado civil'
print(info_usuario)  # Saída: {'nome': 'Altemir', 'idade': 25, 'interesses': ['programação', 'jogos de computador', 'cinema'], 'faz faculdade': True, 'profissão': 'Desenvolvedor'}

# Podemos limpar todo o dicionário usando o método clear()
info_usuario.clear()  # Limpa todos os itens do dicionário 
print(info_usuario)  # Saída: {} (dicionário vazio)

# Temos o metodo setdefault() que retorna o valor da chave se existir, ou define um valor padrão se não existir
info_usuario = {
    "nome": "Altemir",
    "idade": 24,
    "sexo": "Masculino"
}
# Usando setdefault para obter o valor da chave 'profissão' ou definir um valor padrão
profissao = info_usuario.setdefault("profissão", "Desenvolvedor")
print(profissao)  # Saída: Desenvolvedor (valor padrão definido) 
# Verificando o dicionário após o uso de setdefault
print(info_usuario)  # Saída: {'nome': 'Altemir', 'idade': 24, 'sexo': 'Masculino', 'profissão': 'Desenvolvedor'}

# Podemos usar setdefault para definir um valor padrão para uma chave que já existe
profissao = info_usuario.setdefault("profissão", "Analista")
print(profissao)  # Saída: Desenvolvedor (valor existente retornado)    
# Verificando o dicionário após o uso de setdefault
print(info_usuario)  # Saída: {'nome': 'Altemir', 'idade': 24, 'sexo': 'Masculino', 'profissão': 'Desenvolvedor'}

# Podemos usar o método update() para atualizar várias chaves de uma vez