
# No proprio python ja temos como fazer alguns calculos por ele proprio:
    # adição(+); subtração (-); multiplicação(*); divisão(/); divisão com resultado inteiro(//); resto da divisão(%); exponenciação(**)

print("Bem-vindo a sua calculadora do python! ")
n1 = float(input("Insira aqui seu primeiro número: "))
n2 = float(input("Agora insira seu segundo número: "))

soma = (n1+n2)
sub = (n1-n2)
mult = (n1*n2)
div = (n1/n2)
div_int = (n1//n2)
rest_div = (n1%n2)
exp = (n1**n2)

print("--- Aqui estão seus resultados ---")
print(f'A soma dos seus números é: {soma}')
print(f"A subtração dos seus números é: {sub}")
print(f'A multiplicação dos seu números é: {mult}')
print(f'A divisão dos seus números é: {div}')
print(f'A divisão com resultado inteiro é: {div_int}')
print(f'O resto da divisão é: {rest_div}')
print(f'A exponênciação é: {exp}')
