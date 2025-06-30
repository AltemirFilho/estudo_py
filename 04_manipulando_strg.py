# Vamos aqui ver alguma formas de manipular strings
# É importante ter esse conhecimento para minimizar ou até mesmo evitar erro em entradas, dificultando o crash
# Manipular strings tembem ajudam a melhora a interação entre sistema e usuário

texto_para_manipular = "aprender python é Divertido"
print(texto_para_manipular)
print(texto_para_manipular.upper()) # (.upper()) deixa toda string em caixa alta
print(texto_para_manipular.lower()) # (.lower()) deixa toda string em caixa baixa
print(texto_para_manipular.capitalize()) # (.capitalize()) deixa a primeira leta da string em caixa alta
print(texto_para_manipular.title()) # (.title()) deixa a primeira letra de cada palavra da string em ccaixa alta
print(texto_para_manipular.swapcase()) # (.swapcase()) altera tudo que esta em caixa baixa na string para caixa alta e vice-versa
print(texto_para_manipular.count("p")) # (.count("_")) irá contar a quantidade de caracteres ou palavras escolhidos na sting
print(texto_para_manipular.find("é")) # (.find("_")) nos dirá a exata posição onde o que selecionamos se encontra na string, vale lembrar que espaço em branco tambem conta comom posição
print(texto_para_manipular.replace("Divertido", "empolgante")) # (.replace("_","_")) faz a troca de algo especifico da string por algo que o programador queira


# Vale ressaltar que após o modificador escolhido devemos colocar () ao fim do modificador para que esse seja realmente executado