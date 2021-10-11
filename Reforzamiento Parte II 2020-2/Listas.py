# maximo de una lista

lista = [-3.0, -9.0, -0.1, -2.0 , -5.0]
i = 0
maximo = lista[i]
while i < len(lista):
    if lista[i] > maximo:
        maximo = lista[i]
    i += 1
print(maximo)


# minimo 
lista = [-3.0, -9.0, -0.1, -2.0 , -5.0]
i = 0
minimo = lista[i]
while i < len(lista):
    if lista[i] < minimo:
        minimo = lista[i]
    i += 1
print(minimo)

# Ordenar
lista = [-3.0, -9.0, -0.1, -2.0 , -5.0]
lista_ordenada = []
largo = len(lista)
while len(lista_ordenada) != largo:
    i = 0
    minimo = lista[i]
    while i < len(lista):
        if lista[i] < minimo:
            minimo = lista[i]
        i += 1
    lista.remove(minimo)
    lista_ordenada.append(minimo)
print(lista_ordenada)
