# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".
n = int(input("Digite um valor para n: "))
x = 10
y = 1
sum = 0
while(n//x != 0):  
    x = x * 10
    y = y + 1
x = x//10
ant = n//x
n = n - x * ant
x = x//10
y = y - 1 
resp = False
while(y > 0):
    prox = n//x
    if(ant == prox): resp = True
    ant = prox
    sum = sum + (n//x)
    n = n - x * ant
    x = x//10
    y = y - 1
if resp: print("sim")
else: print("não")