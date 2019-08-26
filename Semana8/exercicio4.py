# Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.
def inverte(vetor):
    for i in range(len(vetor)):
        if(len(vetor)==1):
            vetorin.append(vetor[0])
        else:
            if(i != 0):
                if(i != (len(vetor)-1)):
                    vetorin.append(vetor[-i])
                else:
                    vetorin.append(vetor[-i])
                    vetorin.append(vetor[0])            
    return vetorin
def salva_numero(n):
    vetor.append(n)
def main():
    x = 1
    while(x != 0):
        x = int(input("Digite um numero: "))
        if x != 0:
            salva_numero(x)
        else:
            return inverte(vetor)
vetor = []
vetorin = []
main()
for i in range(len(vetorin)):
     print(vetorin[i])