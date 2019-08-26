# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
# Note que
# vogal("a") deve devolver True
# vogal("b") deve devolver False
# vogal("E") deve devolver True
# Os valores True e False devolvidos devem ser do tipo bool (booleanos)
# Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.
def vogal(txt):
    vogals = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    if txt in vogals:
        return True
    else:
        return False
print(vogal(input("Digite a sua letra:")))