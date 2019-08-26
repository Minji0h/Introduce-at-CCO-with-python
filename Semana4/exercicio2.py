# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
n = int(input("Digite o valor de n: "))
y = 1
while(n > 0):
    print(y)
    y = y + 2
    n = n - 1
    
    