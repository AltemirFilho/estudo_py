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