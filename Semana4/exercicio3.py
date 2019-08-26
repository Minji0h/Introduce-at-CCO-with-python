# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída
n = int(input("Digite um valor para n: "))
x = 10
y = 1
sum = 0
while(n//x != 0):  
    x = x * 10
    y = y + 1
x = x//10
while(y > 0):
    div = n//x
    sum = sum + (n//x)
    n = n - x * div
    x = x//10
    y = y - 1
print(sum)
