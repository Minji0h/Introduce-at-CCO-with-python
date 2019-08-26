# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
# Note que
# maior_primo(100) deve devolver 97
# maior_primo(7) deve devolver 7
# Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando se o número é primo ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.
def ehprimo(n):
    d = 2
    metade = n//2
    primo = True
    while d < metade + 1:
        if n % d == 0:
            primo = False
        d = d + 1
    return primo
def maior_primo(n):
    maior = n
    primo = False
    while n > maior//2 - 1 and not primo:
        if ehprimo(n):
            maior = n
            primo = True
        n = n - 1
    return maior
n = int(input("Digite o numero"))
print(maior_primo(n))
