def n_primos(n):
    i = 2
    qtd = 0
    while(i<=n):
        eh_primo = ehprimo(i)
        if eh_primo:
            qtd = qtd + 1
        i = i + 1
    return qtd
def ehprimo(n):
    d = 2
    metade = n//2
    primo = True
    while d < metade + 1:
        if n % d == 0:
            primo = False
        d = d + 1
    return primo
n = 0
n = int(input("Digite um numero: ")) 
while(n<2):
    print("Numero invalido!")
    n = int(input("Digite um numero: "))
print(n_primos(n))

