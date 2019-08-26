#Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
def remove_repetidos(x):
    x.sort()
    i = 1
    y = len(x)
    print(x)
    while y > i:
        ant = x[i-1]
        prox = x[i]
        while(ant == prox and i != y):
            del x[i]
            y = y - 1
            print(x)
            ant = x[i-1]
            prox = x[i]
        i = i + 1
    return x
print(remove_repetidos([7,3,33,12,3,3,3,7,12,100]))

