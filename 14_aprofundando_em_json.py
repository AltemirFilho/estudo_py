# Aqui vamos aprofundar no JSON
# Entender como deixar a formatação mais legível para humanos
# Vamos criar um dicionário com mais dados e mais complexidade

import json # Sempre importe os modulos necessários antes de começar a codar

# Dicionário com dados mais complexos com dicionários e listas aninhados
dados_dev= {
    'nome': 'Altemir',
    'idade': 24,
    'cidade': 'Aracaju',
    'profissao': 'Programador',
    'habilidades': ['Python', 'JavaScript', 'SQL'],
    'experiencia': {
        'empresa1': {
            'nome': 'Empresa A',
            'cargo': 'Desenvolvedor',
            'ano_inicio': 2015,
            'ano_fim': 2018
        },
        'empresa2': {
            'nome': 'Empresa B',
            'cargo': 'Analista',
            'ano_inicio': 2019,
            'ano_fim': 2021
        }
    }
}

with open('dados_dev.json', 'w') as arquivo:
    # Salvando os dados em um arquivo JSON com formatação legível
    # 'w' indica que estamos abrindo o arquivo para escrita, w vem de write
    json.dump(dados_dev, arquivo, indent=4, ensure_ascii=False)
    # indent=4 deixa o JSON mais legível, com 4 espaços de indentação
    # ensure_ascii=False permite caracteres especiais como acentos

# Agora os dados estão salvos no arquivo dados_dev.json
# Podemos verificar o conteúdo do arquivo para confirmar que os dados foram salvos corretamente
with open('dados_dev.json', 'r') as arquivo:
    dados_lidos = json.load(arquivo)
    print(dados_lidos)
    # Lê o conteúdo do arquivo e converte de volta para um dicionário
    # Exibe o conteúdo lido do arquivo

# Ainda podemos explorar mais sobre o JSON
# Vamos adicionar mais dados ao dicionário
dados_dev['projetos'] = [
    {
        'nome': 'Projeto A',
        'descricao': 'Descrição do Projeto A',
        'ano': 2020
    },
    {
        'nome': 'Projeto B',
        'descricao': 'Descrição do Projeto B',
        'ano': 2021
    }
]

    # Salvando os dados atualizados no arquivo JSON
with open('dados_dev.json', 'w') as arquivo:
    json.dump(dados_dev, arquivo, indent=4, ensure_ascii=False) 
    # Atualiza o arquivo com os novos dados
    # Agora o arquivo dados_dev.json contém os dados atualizados

# Podemos verificar novamente o conteúdo do arquivo para confirmar a atualização
with open('dados_dev.json', 'r') as arquivo:
    dados_lidos = json.load(arquivo)
    print(dados_lidos)

# Vamos aprender agora outras formas de manipular os dados JSON
# Vamos criar uma função para adicionar uma nova habilidade
def adicionar_habilidade(habilidade): # Aqui criamos uma função que recebe uma habilidade como parâmetro
    dados_dev['habilidades'].append(habilidade) # Adiciona a nova habilidade à lista de habilidades
    with open('dados_dev.json', 'w') as arquivo: # Salvando os dados atualizados no arquivo JSON
        json.dump(dados_dev, arquivo, indent=4, ensure_ascii=False) # Atualiza o arquivo com os novos dados
        # json.dump converte o dicionário em uma string JSON e escreve no arquivo

# Percena que a estrutura segue amesma ideia da de dicionários e listas do proprio Python
# Vamos adicionar uma nova habilidade
adicionar_habilidade('Java') 
# Podemos verificar novamente o conteúdo do arquivo para confirmar a atualização
with open('dados_dev.json', 'r') as arquivo:
    dados_lidos = json.load(arquivo)
    print(dados_lidos)
    # Verificando se a nova habilidade foi adicionada
    if 'Java' in dados_lidos['habilidades']:
        print("A habilidade 'Java' foi adicionada com sucesso!")
    else:
        print("A habilidade 'Java' não foi encontrada.")
        print("Verifique se a habilidade foi adicionada corretamente.")
    
