# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
# longe
# na saída. Caso o contrário, quando a distância for menor que 10, imprima
# perto
from math import sqrt
Ax = float(input('Digite a cordenada x do primeiro ponto: '))
Ay = float(input('Digite a cordenada y do primeiro ponto: '))

Bx = float(input('Digite a cordenada y do segundo ponto: '))
By = float(input('Digite a cordenada x do segundo ponto: '))

distAB = sqrt(((Bx-Ax)**2) + ((By-Ay)**2))

if(distAB >= 10):
    print("longe")
else:
    print("perto")