# Aqui vamos fazer uma pratica utilizndo tudo que vimos para montar um siatema de uma loja
import json

produtos_cadastrados = {
    "bolas_tennis": [
        {
            'marca': 'Wilson',
            'preco': 20.00,
            'quantidade': 40,
            'descricao': 'Bola de tênis Wilson US Open, ideal para jogos profissionais.'
        },
        {
            'marca': 'Head',
            'preco': 22.50,
            'quantidade': 30,
            'descricao': 'Bola de tênis Head Tour, excelente para treinos e competições.'
        },
        {
            'marca': 'Babolat',
            'preco': 25.00,
            'quantidade': 20,
            'descricao': 'Bola de tênis Babolat Pure Drive, para jogadores exigentes.'
        }
    ],
    "raquetes_tennis": [
        {
            'marca': 'Wilson',
            'preco': 1500.00,
            'quantidade': 15,
            'descricao': 'Raquete de tênis Wilson Blade, ideal para controle e precisão.'
        },
        {
            'marca': 'Head',
            'preco': 1600.00,
            'quantidade': 10,
            'descricao': 'Raquete de tênis Head Graphene 360, para jogadores avançados.'
        },
        {
            'marca': 'Babolat',
            'preco': 1700.00,
            'quantidade': 5,
            'descricao': 'Raquete de tênis Babolat Pure Aero, para jogadores agressivos.'
        }
    ],
    "overgrips_tennis": [
        {
            'marca': 'Wilson',
            'preco': 30.00,
            'quantidade': 100,
            'descricao': 'Overgrip Wilson Pro, para melhor aderência e conforto.'
        },
        {
            'marca': 'Head',
            'preco': 35.00,
            'quantidade': 80,
            'descricao': 'Overgrip Head HydroSorb, para uma pegada mais macia.'
        },
        {
            'marca': 'Babolat',
            'preco': 40.00,
            'quantidade': 60,
            'descricao': 'Overgrip Babolat VS Grip, para uma sensação de toque superior.'
        }
    ],
    "raqueteiras_tennis": [
        {
            'marca': 'Wilson',
            'preco': 400.00,
            'quantidade': 20,
            'descricao': 'Raqueteira Wilson, para transporte seguro de raquetes.'
        },
        {
            'marca': 'Head',
            'preco': 450.00,
            'quantidade': 15,
            'descricao': 'Raqueteira Head, para proteção e estilo.'
        },
        {
            'marca': 'Babolat',
            'preco': 500.00,
            'quantidade': 10,
            'descricao': 'Raqueteira Babolat, para jogadores exigentes.'
        }
    ]
}

with open('produtos_cadastrados.json', 'w') as arquivo:
    json.dump(produtos_cadastrados, arquivo, indent=4) # Salva os dados no arquivo JSON com formatação legível

def listar_produtos():
    with open('produtos_cadastrados.json', 'r') as arquivo:
        produtos = json.load(arquivo) # Lê os dados do arquivo JSON
        print("Produtos disponíveis:")
        for categoria, itens in produtos.items(): # Itera sobre cada categoria e seus itens
            print(f"\nCategoria: {categoria}")
            for item in itens:
                print(f"Marca: {item['marca']}\nPreço: R${item['preco']:.2f}\nQuantidade: {item['quantidade']}\nDescrição: {item['descricao']}\n")

