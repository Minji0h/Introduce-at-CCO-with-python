# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".
# Exemplos:
# Digite um número inteiro: 11
# primo
# Digite um número inteiro: 12
# não primo
n = int(input("Digite um numero: "))
primo = True
i = 2
while(i <= n//2):
    if n%i == 0: primo = False
    i = i + 1
if primo:
    print("primo")
else:
    print("não primo")
