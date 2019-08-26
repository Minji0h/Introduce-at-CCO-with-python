# Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.
# Note que
# maximo(3,4) deve devolver 4
# maximo(0,-1) deve devolver 0
def maximo(x,y):
    if(x>y):
        return x
    else:
        return y
x = int(input("Digite o primeiro numero"))
y = int(input("Digite o segundo numero"))
print(maximo(x,y))