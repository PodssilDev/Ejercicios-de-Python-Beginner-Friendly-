'''
Parte A
'CTGA CTGA AATT GGGC CTGG CCCC'
True
['CTGA','CTGA','AATT']

'CTGA XCGA CGAT GGTA ACCC CCPC TTAA'
False
'''

bases = ["A","C","G","T"]
def valida(cadena):
    lista_cadena = cadena.split()
    i = 0
    while i < len(lista_cadena):
        bloque = lista_cadena[i]
        j = 0
        while j < len(bloque):
            if bloque[j] not in bases:
                return False
            else:
                j+=1
        i+=1
booleano = valida("CTGA XCGA CGAT GGTA ACCC CCPC TTAA")
if booleano != False:
    booleano = True
print(booleano)

    

'''
Parte B
'CTGA CTGA AATT GGGC CTGG CCCC', 'A'
4
'''


def cantidad(cadena,base):
    lista_cadena = cadena.split()
    i = 0
    contador = 0
    while i < len(lista_cadena):
        bloque = lista_cadena[i]
        j = 0
        while j < len(bloque):
            if bloque[j] == base:
                contador = contador + 1
            j+=1
        i+=1
    return contador
numero = cantidad("CTGA CTGA AATT GGGC CTGG CCCC", "A")
print(numero)
