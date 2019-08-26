#############################################################
#############################################################
################                             ################
################      Variaveis Globais      ################
################                             ################
#############################################################
#############################################################
import re
ass_padrao = []
plv_texto = []
unic_texto = 0
dife_texto = 0
set_texto = []
frs_texto = []
assinatura_texto = []
maior_chance = 0
menor_sub = 900
#############################################################
#############################################################
################                             ################
################        Chama classes        ################
################                             ################
#############################################################
#############################################################
def chama_classes():
    le_assinatura()
    le_textos()
    for i in range(len(textos)):
        ass_texto.append(calcula_assinatura(textos[i]))
        avalia_textos(ass_texto[i],ass_padrao)
#############################################################
#############################################################
################                             ################
################       Caracteristicas       ################
################                             ################
#############################################################
#############################################################
def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    ass_padrao.append(float(input("Entre o tamanho medio de palavra:")))
    ass_padrao.append(float(input("Entre a relação Type-Token:")))
    ass_padrao.append(float(input("Entre a Razão Hapax Legomana:")))
    ass_padrao.append(float(input("Entre o tamanho médio de sentença:")))
    ass_padrao.append(float(input("Entre a complexidade média da sentença:")))
    ass_padrao.append(float(input("Entre o tamanho medio de frase:")))
#############################################################
#############################################################
################                             ################
################      Entrada dos textos     ################
################                             ################
#############################################################
#############################################################
def le_textos():
    i = 1
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    avalia_textos(textos,ass_padrao)
#############################################################
#############################################################
################                             ################
################   Calcula a assinatura do   ################
################           texto             ################
################                             ################
#############################################################
#############################################################
def calcula_assinatura(texto):
    assinatura_texto = []
    calcula_quantidades_texto(texto)
    assinatura_texto.append(calcula_tamanho_medio_palavra(plv_texto))
    assinatura_texto.append(calcula_type_token(plv_texto,dife_texto))
    assinatura_texto.append(calcula_razao_hapax_legomana(unic_texto, plv_texto))
    assinatura_texto.append(calcula_tamanho_medio_setencas(set_texto))
    assinatura_texto.append(calcula_complexidade_sentenca(set_texto,frs_texto))
    assinatura_texto.append(calcula_tamanho_medio_frases(frs_texto))
    return assinatura_texto
#############################################################
#############################################################
################                             ################
################   Calcula a quantidade de:  ################
################          Palavras           ################
################          Frases             ################
################          Sentenças          ################
################        Em cada texto        ################
################                             ################
#############################################################
#############################################################
def calcula_quantidades_texto(texto):
    global set_texto
    global plv_texto
    global dife_texto
    global frs_texto
    global unic_texto
    set_texto = separa_sentencas(texto)
    for i in range(len(set_texto)):
        frs_texto = frs_texto + separa_frases(set_texto[i])
    for j in range(len(frs_texto)):
        plv_texto = plv_texto + separa_palavras(frs_texto[j])
    dife_texto = n_palavras_diferentes(plv_texto)
    unic_texto = n_palavras_unicas(plv_texto)
    print("-------------------")
    print(unic_texto)
#############################################################
#############################################################
################                             ################
################      Divide sentenças       ################
################                             ################
#############################################################
#############################################################
def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto) 
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas
#############################################################
#############################################################
################                             ################
################        Divide frases        ################
################                             ################
#############################################################
#############################################################
def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)
#############################################################
#############################################################
################                             ################
################       Divide palavras       ################
################                             ################
#############################################################
############################################################
def separa_palavras(frase):
    teste = frase.split()
    return teste
#############################################################
#############################################################
################                             ################
################       Palavras Unicas       ################
################                             ################
#############################################################
#############################################################
def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas
#############################################################
#############################################################
################                             ################
################     Palavras Diferentes     ################
################                             ################
#############################################################
#############################################################
def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)
#############################################################
#############################################################
################                             ################
################    Calcula tamanho medio    ################
################        das palavras         ################
################                             ################
#############################################################
#############################################################
def calcula_tamanho_medio_palavra(palavras):
    soma = 0
    j = 0
    for i in range(len(palavras)):
        soma = soma + len(palavras[i])
    return soma/len(palavras)
#############################################################
#############################################################
################                             ################
################     Calcula type-token      ################
################                             ################
#############################################################
#############################################################
def calcula_type_token(palavras, diferentes):
    return diferentes/len(palavras)
#############################################################
#############################################################
################                             ################
################     Calcula razão hapax     ################
################           legomana          ################
################                             ################
#############################################################
#############################################################
def calcula_razao_hapax_legomana(unicas, palavras):
    print(unicas)
    print(len(palavras))
    return unicas/len(palavras)
#############################################################
#############################################################
################                             ################
################    Calcula tamanho medio    ################
################         das sentencas       ################
################                             ################
#############################################################
#############################################################
def calcula_tamanho_medio_setencas(setencas):
    soma = 0
    for i in range(len(setencas)):
        soma = soma + len(setencas[i])
    return soma/(len(setencas))
#############################################################
#############################################################
################                             ################
################    Calcula complexidade     ################
################         das sentencas       ################
################                             ################
#############################################################
#############################################################
def calcula_complexidade_sentenca(sentencas, frases):
    sentenca = len(sentencas)
    frase = len(frases)
    return frase/sentenca
#############################################################
#############################################################
################                             ################
################      Calcula medio das      ################
################            frases           ################
################                             ################
#############################################################
#############################################################
def calcula_tamanho_medio_frases(frases):
    soma = 0
    for i in range(len(frases)):
        soma = soma + len(frases[i])
    return soma/len(frases)

def compara_assinatura(as_a, as_b):
    soma = 0
    for i in range(len(as_b)):
        soma = soma + abs(as_a[i]-as_b[i])
        print("---------------")
        print(soma)
    sub = soma/6
    return round(sub,2)
def avalia_textos(textos, ass_cp):
    global menor_sub
    global maior_chance
    for i in range(len(textos)):
        ass_texto = calcula_assinatura(textos[i])
        print(ass_texto)
        sub = (compara_assinatura(ass_texto,ass_cp))
        if sub < menor_sub:
               menor_sub = sub
               maior_chance = i
    imprime(maior_chance)
    return maior_chance + 1
def imprime(i):
    print("O autor do texto "+ str(i+1) +" está infectado com COH-PIAH")
