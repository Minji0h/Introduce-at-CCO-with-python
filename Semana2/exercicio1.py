# Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.
# Observação: a saída deve estar no formato: "perímetro: x - área: y"
# Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:
# Exemplo:
# Entrada de Dados: 
# Digite o valor correspondente ao lado de um quadrado: 3
# Saída de Dados:
# perímetro: 12 - área: 9
lado = input("Digite o tamanho do lado do quadrado")
area = int(lado) ** 2
perimetro = int(lado) * 4
print("perímetro: " + str(perimetro) + " - área: " + str(area))
