import math
def soma_hipotenusas(n):
    i = 1
    soma = 0
    while(i <= n):
        if(eh_hipotenusa(i)):
            soma = soma + i
        i = i + 1
    return soma
def eh_hipotenusa(n):
    a = 1
    hipotenusa = False
    
    while(a<=n):
        b = 1
        while(b<=n):
            c = math.hypot(a, b)
            if c == n:
                hipotenusa = True
            b = b + 1
        a = a + 1
    return hipotenusa
n = int(input("Digite um numero: "))
print(soma_hipotenusas(n))
