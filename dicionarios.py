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
info_usuario.update({
    "cidade": "São Paulo",
    "estado": "SP"
})  # Atualizando várias chaves de uma vez 
print(info_usuario)  # Saída: {'nome': 'Altemir', 'idade': 24, 'sexo': 'Masculino', 'profissão': 'Desenvolvedor', 'cidade': 'São Paulo', 'estado': 'SP'}

# Podemos usar o método copy() para criar uma cópia do dicionário
info_usuario_copia = info_usuario.copy()  # Criando uma cópia do dicionário
print(info_usuario_copia)  # Saída: {'nome': 'Altemir', 'idade': 24, 'sexo': 'Masculino', 'profissão': 'Desenvolvedor', 'cidade': 'São Paulo', 'estado': 'SP'}

# Vamos explorar mais algumas operações avançadas com dicionários
# vamos criar um dicionario onde cada chve cotem uma lista de valores e vamos adicionar valores a essa lista
info_produtos = {
    "frutas": ["maçã", "banana", "laranja"],
    "legumes": ["cenoura", "batata", "brócolis"],
    "carnes": ["frango", "bife", "peixe"]
}  
# Podemos adicionar um novo item à lista de frutas
info_produtos["frutas"].append("uva")
print(info_produtos)  # Saída: {'frutas': ['maçã', 'banana', 'laranja', 'uva'], 'legumes': ['cenoura', 'batata', 'brócolis'], 'carnes': ['frango', 'bife', 'peixe']}

# Podemos adicionar um novo item à lista de legumes
info_produtos["legumes"].append("abobrinha")
print(info_produtos)  # Saída: {'frutas': ['maçã', 'banana', 'laranja', 'uva'], 'legumes': ['cenoura', 'batata', 'brócolis', 'abobrinha'], 'carnes': ['frango', 'bife', 'peixe']}   

# vamos entrender agora como podemos fazer o usuarío interagir com o dicionário
# Vamos criar uma função para adicionar um novo produto ao dicionário
def adicionar_produto(categoria, produto): # A função recebe a categoria e o produto a ser adicionado, essas são variáveis que o usuário irá informar
    if categoria in info_produtos: # Verifica se a categoria já existe no dicionário
        info_produtos[categoria].append(produto) # Se existir, adiciona o produto à lista da categoria
    else:
        info_produtos[categoria] = [produto] # Se não existir, cria uma nova lista com o produto
    print(f"Produto '{produto}' adicionado à categoria '{categoria}'.") 
    print("Dicionário atualizado:", info_produtos)  # Exibe o dicionário atualizado

# Vamos criar uma função para remover um produto de uma categoria
def remover_produto(categoria, produto):       
    if categoria in info_produtos and produto in info_produtos[categoria]: # Verifica se a categoria e o produto existem
        info_produtos[categoria].remove(produto) # Remove o produto da lista da categoria
        print(f"Produto '{produto}' removido da categoria '{categoria}'.")
    else:
        print(f"Produto '{produto}' não encontrado na categoria '{categoria}'.") # Mensagem de erro se o produto não existir
    print("Dicionário atualizado:", info_produtos)  # Exibe o dicionário atualizado 

# Vamos criar uma função para exibir os produtos de uma categoria
def exibir_produtos(categoria):
    if categoria in info_produtos: # Verifica se a categoria existe no dicionário
        print(f"Produtos na categoria '{categoria}':") 
        for produto in info_produtos[categoria]: # Itera sobre os produtos da categoria 
            print(f" - {produto}")
    else:
        print(f"Categoria '{categoria}' não encontrada.") # Mensagem de erro se a categoria não existir

# Vamos criar uma função para exibir todas as categorias e seus produtos
def exibir_todas_categorias():
    if info_produtos:  # Verifica se o dicionário não está vazio
        print("Categorias e produtos:")
        for categoria, produtos in info_produtos.items():  # Itera sobre as categorias e seus produtos
            print(f"{categoria}: {', '.join(produtos)}")  # Exibe a categoria e os produtos separados por vírgula, .join(produtos) converte a lista de produtos em uma string separada por vírgulas
    else:
        print("Nenhuma categoria encontrada.")  # Mensagem se o dicionário estiver vazio

# Vamos testar as funções criadas
adicionar_produto("frutas", "kiwi")  # Adiciona kiwi à categoria frutas
adicionar_produto("laticínios", "leite")  # Adiciona leite à nova categoria laticínios
remover_produto("frutas", "banana")  # Remove banana da categoria frutas            
exibir_produtos("frutas")  # Exibe os produtos da categoria frutas
exibir_produtos("laticínios")  # Exibe os produtos da categoria l

# Vamos fazer uma interação com o usuário para adicionar, remover e exibir produtos
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Exibir produtos de uma categoria")
    print("4. Exibir todas as categorias e produtos")
    print("5. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        categoria = input("Informe a categoria: ")
        produto = input("Informe o produto: ")
        adicionar_produto(categoria, produto)
    elif opcao == "2":
        categoria = input("Informe a categoria: ")
        produto = input("Informe o produto: ")
        remover_produto(categoria, produto)
    elif opcao == "3":
        categoria = input("Informe a categoria: ")
        exibir_produtos(categoria)
    elif opcao == "4":
        exibir_todas_categorias()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
# Fim do código de interação com o usuário

# Vamos explorar mais algumas operações avançadas com dicionários
# Vamos criar um dicionário de produtos com preços
info_produtos_precos = {
    "frutas": {
        "banana": 1.50,
        "maçã": 2.00,
        "kiwi": 3.00
    },
    "laticínios": {
        "leite": 4.00,
        "queijo": 5.00
    }
}
# Veja que acima criamos um dicionário onde cada chave contém outro dicionário, isso é conhecido como dicionário aninhado
# Podemos acessar os preços dos produtos usando chaves aninhadas
print("Preço da banana:", info_produtos_precos["frutas"]["banana"])
print("Preço do leite:", info_produtos_precos["laticínios"]["leite"])
# Saída:
# Preço da banana: 1.5
# Preço do leite: 4.0   

# Podemos adicionar um novo produto com preço
info_produtos_precos["frutas"]["laranja"] = 2.50  # Adicionando laranja à categoria frutas com preço
print("Dicionário atualizado:", info_produtos_precos)  # Exibe o dicionário atualizado

# Podemos remover um produto com preço
info_produtos_precos["laticínios"].pop("queijo")  # Removendo queijo da categoria laticínios
print("Dicionário atualizado:", info_produtos_precos)  # Exibe o dicionário atualizado  

# Podemos exibir todos os produtos e seus preços
def exibir_produtos_precos():
    if info_produtos_precos:  # Verifica se o dicionário não está vazio
        print("Produtos e preços:")
        for categoria, produtos in info_produtos_precos.items():  # Itera sobre as categorias e seus produtos, items é o conjunto de chaves e valores
            # Exibe a categoria e os produtos com seus preços
            print(f"{categoria}:")
            for produto, preco in produtos.items():  # Itera sobre os produtos e seus preços
                print(f" - {produto}: R$ {preco:.2f}")  # Exibe o produto e seu preço formatado
    else:
        print("Nenhum produto encontrado.")  # Mensagem se o dicionário estiver vazio
# Vamos testar a função de exibição de produtos e preços
exibir_produtos_precos()  # Exibe todos os produtos e seus preços
# Fim do código de exibição de produtos e preços

# Vamos explorar mais algumas operações avançadas com dicionários
# Vamos criar um dicionário de usuários com informações adicionais
info_usuarios = {
    "usuario1": {
        "nome": "Altemir",
        "idade": 24,
        "email": "altemir@example.com"
    },
    "usuario2": {
        "nome": "Beatriz",
        "idade": 30,
        "email": "beatriz@example.com"
    }
}   
# Podemos acessar as informações de um usuário específico
print("Nome do usuário1:", info_usuarios["usuario1"]["nome"])  # Saída: Nome do usuário1: Altemir
print("Idade do usuário1:", info_usuarios["usuario1"]["idade"])  # Saída: Idade do usuário1: 24
print("Email do usuário1:", info_usuarios["usuario1"]["email"])  # Saída: Email do usuário1: altemir@example.com    

# Podemos adicionar um novo usuário com informações adicionais
info_usuarios["usuario3"] = {
    "nome": "Carlos",
    "idade": 28,
    "email": "carlos@example.com"
}   
print("Dicionário atualizado:", info_usuarios)  # Exibe o dicionário atualizado

# Podemos remover um usuário específico
info_usuarios.pop("usuario2")  # Removendo o usuário2   
print("Dicionário atualizado:", info_usuarios)  # Exibe o dicionário atualizado

# Podemos exibir todos os usuários e suas informações
def exibir_usuarios():
    if info_usuarios:  # Verifica se o dicionário não está vazio
        print("Usuários:")
        for usuario, info in info_usuarios.items():  # Itera sobre os usuários e suas informações
            # Exibe o usuário e suas informações
            print(f"{usuario}:")
            print(f" - Nome: {info['nome']}") # Usamos info para acessar as informações do usuário
            print(f" - Idade: {info['idade']}")
            print(f" - Email: {info['email']}")
    else:
        print("Nenhum usuário encontrado.")  # Mensagem se o dicionário estiver vazio

# Vamos testar a função de exibição de usuários
exibir_usuarios()  # Exibe todos os usuários e suas informações
# Fim do código de exibição de usuários

# Vamos entender como fazer o usuário interagir com o dicionário de usuários
while True:
    print("\nMenu:")
    print("1. Adicionar usuário")
    print("2. Remover usuário")
    print("3. Exibir usuários")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Adicionar usuário
        usuario = input("Digite o nome do usuário: ") # Aqui definimos a variável usuario que irá armazenar o nome do usuário
        if usuario in info_usuarios:
            print("Usuário já existe. Tente novamente.")
            continue  # Aqui continuamos para a próxima iteração do loop se o usuário já existir
        # Coletando informações adicionais do usuário
        idade = int(input("Digite a idade do usuário: ")) 
        email = input("Digite o email do usuário: ")
        # Agora vamos adicionar o usuário ao dicionário
        # Vamos basicamente colocar as informações que colocamos nas variáveis dentro do dicionário
        # info_usuarios é o dicionário que armazena as informações dos usuários, pois queremos que as informações sejam armazenadas dentro do dicionário
        info_usuarios[usuario] = {
            "nome": usuario,
            "idade": idade,
            "email": email
        }
        print("Usuário adicionado com sucesso!")

    elif opcao == "2":
        # Remover usuário
        usuario = input("Digite o nome do usuário a ser removido: ")
        info_usuarios.pop(usuario, None) # O none é usado para evitar erro caso o usuário não exista
        if usuario not in info_usuarios:
            print("Usuário não encontrado.")
            continue
        print("Usuário removido com sucesso!")

    elif opcao == "3":
        # Exibir usuários
        exibir_usuarios()

    elif opcao == "4":
        # Sair
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
# Fim do código de interação com o usuário para o dicionário de usuários

# Vamos explorar mais algumas operações avançadas com dicionários
# Vamos criar um dicionário de produtos com categorias e preços
produtos = {
    "produto1": {
        "nome": "Notebook",
        "categoria": "Eletrônicos",
        "preco": 2500.00
    },
    "produto2": {
        "nome": "Smartphone",
        "categoria": "Eletrônicos",
        "preco": 1500.00
    },
    "produto3": {
        "nome": "Camiseta",
        "categoria": "Vestuário",
        "preco": 79.90
    }
}

# Podemos acessar as informações de um produto específico
# definimos produto1 como a chave do dicionário, e dentro dele temos as informações do produto
# Aqui mostramos ao sistema que queremos acessar o nome, categoria e preço do produto1
print("Nome do produto1:", produtos["produto1"]["nome"])  # Saída: Notebook
print("Categoria do produto1:", produtos["produto1"]["categoria"])  # Saída: Eletrônicos
print("Preço do produto1:", produtos["produto1"]["preco"])  # Saída: 2500.0

# Podemos adicionar um novo produto com informações adicionais
produtos["produto4"] = {
    "nome": "Tênis",
    "categoria": "Vestuário",
    "preco": 299.90
}
print("Dicionário atualizado:", produtos)  # Exibe o dicionário atualizado

# Podemos remover um produto específico
produtos.pop("produto2")  # Removendo o produto2
print("Dicionário atualizado:", produtos)  # Exibe o dicionário atualizado

# Podemos exibir todos os produtos e suas informações
def exibir_produtos():
    if produtos:  # Verifica se o dicionário não está vazio
        print("Produtos:")
        for produto, info in produtos.items():  # Itera sobre os produtos e suas informações
            # Exibe o produto e suas informações
            print(f"{produto}:")
            print(f" - Nome: {info['nome']}")
            print(f" - Categoria: {info['categoria']}")
            print(f" - Preço: R$ {info['preco']:.2f}")
    else:
        print("Nenhum produto encontrado.")  # Mensagem se o dicionário estiver vazio
# Vamos testar a função de exibição de produtos
exibir_produtos()  # Exibe todos os produtos e suas informações
# Fim do código de exibição de produtos

# Vamos entender como fazer o usuário interagir com o dicionário de produtos
while True:
    print("\nMenu:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Exibir produtos")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Adicionar produto
        produto = input("Digite o nome do produto: ")
        if produto in produtos:
            print("Produto já existe. Tente novamente.")
            continue  # Continua para a próxima iteração do loop se o produto já existir
        # Coletando informações adicionais do produto
        categoria = input("Digite a categoria do produto: ")
        preco = float(input("Digite o preço do produto: "))
        # Agora vamos adicionar o produto ao dicionário
        produtos[produto] = {
            "nome": produto,
            "categoria": categoria,
            "preco": preco
        }
        print("Produto adicionado com sucesso!")

    elif opcao == "2":
        # Remover produto
        produto = input("Digite o nome do produto a ser removido: ")
        produtos.pop(produto, None)  # O None é usado para evitar erro caso o produto não exista
        if produto not in produtos:
            print("Produto não encontrado.")
            continue
        print("Produto removido com sucesso!")

    elif opcao == "3":
        # Exibir produtos
        exibir_produtos()

    elif opcao == "4":
        # Sair
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
# Fim do código de interação com o usuário para o dicionário de produtos