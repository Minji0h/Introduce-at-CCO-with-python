# Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.
# O programa deve receber os parâmetros a,b, e c da equação ax^2 + bx + c, respectivamente, e imprimir o resultado na saída da seguinte maneira:
# Quando não houver raízes reais imprima:
# esta equação não possui raízes reais
# Quando houver apenas uma raiz real imprima:
# a raiz desta equação é X
# onde X é o valor da raiz
# Quando houver duas raízes reais imprima:
# as raízes da equação são X e Y
# onde X e Y são os valor das raízes.
# Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente, ou seja, X deve ser menor que Y.
from math import sqrt
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
delta = (b ** 2 - (4 * a * c))
if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    x = (-b + sqrt(delta))/2
    print("a raiz desta equação é " + str(x))
else:
    x = (-b + sqrt(delta))/2
    y = (-b - sqrt(delta))/2
    if y > x:
        print("as raízes da equação são " + str(x) + " e " + str(y))
    else:
        print("as raízes da equação são " + str(y) + " e " + str(x))
