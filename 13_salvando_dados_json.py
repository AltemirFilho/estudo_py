# Vamos agregar os dados de um dicionário em um arquivo JSON
# Isso serve para que após o programa ser executado, os dados sejam salvos, permitindo que sejam lidos posteriormente
# Para isso, vamos utilizar a biblioteca json


import json
# Dicionário com os dados que queremos salvar
dados = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

# Salvando os dados em um arquivo JSON
with open('dados.json', 'w') as arquivo: 
    # Usamos with open para garantir que o arquivo seja fechado corretamente
    # 'w' indica que estamos abrindo o arquivo para escrita, w vem de write
    # Se o arquivo não existir, ele será criado. Se já existir, será sobrescrito
    # Usamos as arquivo para indicar que vamos escrever os dados no arquivo
    json.dump(dados, arquivo)
    # Json.dump converte o dicionário em uma string JSON e escreve no arquivo
    # O arquivo ficará salvo na pasta onde o script está sendo executado
    # Isso nos permite salvar os dados de forma estruturada e fácil de ler

# Agora os dados estão salvos no arquivo dados.json
# Podemos verificar o conteúdo do arquivo para confirmar que os dados foram salvos corretamente
# Vamos ler o arquivo para verificar se os dados foram salvos corretamente
with open('dados.json', 'r') as arquivo:
    # 'r' indica que estamos abrindo o arquivo para leitura, r vem de read
    conteudo = json.load(arquivo)
    # Json.load lê o conteúdo do arquivo e converte de volta para um dicionário
    # Isso nos permite acessar os dados como um dicionário novamente, possibilitando manipular os dados lidos
    print(conteudo)
    # Exibe o conteúdo lido do arquivo
# O resultado deve ser: {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
# Isso confirma que os dados foram salvos e lidos corretamente do arquivo JSON

# Agora vamos manipular os dados lidos
conteudo['idade'] += 1  # Incrementa a idade em 1
# Salvando novamente os dados atualizados no arquivo JSON
with open('dados.json', 'w') as arquivo:
    json.dump(conteudo, arquivo)
    # Atualiza o arquivo com os novos dados
# Agora o arquivo dados.json contém os dados atualizados
# Podemos verificar novamente o conteúdo do arquivo para confirmar a atualização    
with open('dados.json', 'r') as arquivo:
    conteudo = json.load(arquivo)
    print(conteudo)
    # Exibe o conteúdo atualizado do arquivo
    # Se abrirmos o arquivo dados.json, veremos que a idade foi incrementada em 1

# Vamos adicionar mais dados ao dicionário
conteudo['profissao'] = 'Engenheiro'
# Salvando novamente os dados atualizados no arquivo JSON
with open('dados.json', 'w') as arquivo:
    json.dump(conteudo, arquivo)
    # Atualiza o arquivo com os novos dados
# Agora o arquivo dados.json contém os dados atualizados
# Podemos verificar novamente o conteúdo do arquivo para confirmar a atualização
with open('dados.json', 'r') as arquivo:
    conteudo = json.load(arquivo)
    print(conteudo)
    # Exibe o conteúdo atualizado do arquivo
    # Se abrirmos o arquivo dados.json, veremos que a profissão foi adicionada
# Isso demonstra como podemos salvar, ler e atualizar dados em um arquivo JSON de forma simples e eficiente
# Agora temos um exemplo completo de como trabalhar com arquivos JSON em Python
# Todas funções dos dicionários podem ser utilizadas normalmente e convertidas para JSON
# Isso nos permite armazenar dados de forma estruturada e fácil de manipular e com sintaxe simples
