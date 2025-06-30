# aprendendo a usar o input
# Sempre que quisermos que tenha uma entrada para o sistema usamos a função input

nome = input("Qual o seu nome? ") # Aqui nomeamos que a variável será preenchida pelo usuário


print(f"Seja bem-vindo, {nome} !") # ((f"_")) f string ns permite printar texto e variáveis dentro, estando essas entre chaves  {}


trabalho = input("Qual sua profissão? ")
cidade = input("Em que cidade você mora? ")


print(f"Então você é o(a) famoso(a) {nome} que é {trabalho} e mora em {cidade}!? Sempre quis te conhecer!") # Um exemplo claro de f string