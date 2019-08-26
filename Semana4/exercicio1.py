# Escreva um programa que receba um número natural n n n na entrada e imprima n! n! n! (fatorial) na saída.
n = int(input("Digite o valor de n: "))
fator = 1 
while(n > 0):
    fator = fator * n
    n = n - 1
print(fator)


